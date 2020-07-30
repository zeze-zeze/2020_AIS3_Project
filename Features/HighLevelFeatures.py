import subprocess
from pwn import *

class HighLevelFeatures():
    def __init__(self, preprocess):
        self.filename = preprocess.filename
        self.block_info = preprocess.block_info
        self.function_info = preprocess.function_info
    
    def displayFunction(self):
        for f in self.function_info:
            print(f)

    def getInstruction(self):
        res = subprocess.check_output(['objdump', '-M', 'intel', '-d', self.filename]).split(b'\n')
        for r in res[:5]:
            print(res)

    def getCallType(self):
        dump = open('dump', 'rb').read().split(b'\n')
        for i in range(len(dump)):
            if b'>:' not in dump[i]:
                continue
            addr = int(dump[i].split()[0], 16)
            calls = []
            j = i + 1
            while j < len(dump):
                if b'>:' in dump[j]: break
                if b'call' in dump[j]:
                    d = dump[j].split()[-1]
                    if b'@plt' not in d:
                        calls.append(0)
                    #else:
                    #    calls.append(collectionsd[split(b'@')[0].split(b'<')[1]])
                j += 1
            
            for f in self.function_info:
                if f['addr'] == addr:
                    f['calls'] = calls
                    break

    def excludeFunction(self):
        l = len(self.function_info)
        while l > 0:
            l -= 1
            if 'calls' not in self.function_info[l]:
                self.function_info.pop(l)

    def getCallOrder(self):
        for f in self.function_info:
            f['call_order'] = {}
            for i in range(3):
                for j in range(3):
                    f['call_order']['{}{}'.format(i, j)] = 0
            now = -1
            for c in f['calls']:
                if now == -1:
                    now = c
                    continue
                f['call_order']['{}{}'.format(now, c)] += 1
