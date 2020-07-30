import angr
from pwn import *

context.log_level = 'CRITICAL'

class StructuralFeatures():
    def __init__(self, preprocess):
        #
        # self.block_info - basic block structure: 
        # preprocess.block_info
        # x: int, seuqential number
        # y: int, outgoing edges, 
        # z: int, loop depth, 
        # w: int, number of instructions,
        # w2: int, number of instructions + number of call instructions
        # block_count: int, the number of blocks after the block
        # instruction_count: int, the number of instructions after the block
        #
        self.block_info = preprocess.block_info
        for block in self.block_info:
            block['w'] = 0
            block['w2'] = 0
            block['x'] = 0
            block['y'] = 0
            block['z'] = 0
            block['node_count'] = 0
            block['instruction_count'] = 0

        self.function_info = preprocess.function_info
        self.filename = preprocess.filename
        self.proj = preprocess.proj
        self.cfg = preprocess.cfg
    
    def display(self):
        for block in self.block_info:
            print(block['index'], block['is_function'], block['ingoing_nodes'], block['outgoing_nodes'], block['w'], block['w2'], block['x'], block['y'], block['z'])

    def getY(self):
        #
        # Check: Count the number of outgoing edges and put into 'y'
        # Complexity: O(n), n = number of nodes
        #
        for block in self.block_info:
            block['y'] = len(block['outgoing_nodes'])

    def getZ(self):
        #
        # Check: Compute loop depth and put into 'z'. 
        # Implement: 
        #     1. Iterate every node n and see whether the ingoing node of n is in dom(n)
        #     2. If the ingoing node of n is in dom(n), then add 1 to each z of the node between n and the ingoing node
        # Complexity: O(fn^2 m), f = number of functions in a program, n = number of nodes in a function, m = number of edges in a function
        #
        def revBFS(bottom, top, function_range):
            #
            # Check: Use reverse BFS to add each node in a loop
            # Complexity: O(m), n = nodes, m = edges
            #
            added = [False for i in range(function_range[1] - function_range[0])]
            stack = [bottom]
            self.block_info[top]['z'] += 1
            while stack:
                now_node = stack.pop()
                if now_node == top or added[now_node - function_range[0]]:
                    continue
                self.block_info[now_node]['z'] += 1
                added[now_node - function_range[0]] = True
                for ingoing_node in self.block_info[now_node]['ingoing_nodes']:
                    if now_node not in self.block_info[ingoing_node]['dominators'] and top in self.block_info[ingoing_node]['dominators'] and function_range[1] > ingoing_node >= function_range[0] and not added[ingoing_node - function_range[0]]:
                        stack.append(ingoing_node)

        def checkAddZ(function_range):
            for j in range(function_range[0], function_range[1]):
                for k in self.block_info[j]['outgoing_nodes']:
                    if k in self.block_info[j]['dominators']:
                        revBFS(j, k, function_range)
                        break

        for func in self.function_info:
            checkAddZ(func['function_range'])

    def getW(self):
        #
        # Check: Count the number of instructions and put into 'w', 
        #        Plus the call insturctions and put into 'w2'
        # Complexity: O(n), n = number of nodes
        #
        binary = open(self.filename, 'rb').read()
        for block in self.block_info:
            block['w'] = block['instructions_num']
            if block['addr'] < len(binary):
                total = disasm(binary[block['addr']:block['addr'] + self.proj.factory.block(block['addr']).size]).count('call')
                block['w2'] = block['w'] + total
