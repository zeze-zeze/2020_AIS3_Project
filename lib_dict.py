#!/usr/bin/env python
import csv
import pickle

reader = csv.reader(open('libtype.csv'))
func_dict = {}
for row in reader:
    func_dict[row[0]] = row[1]

print(func_dict)

types = """Calculation
File Access
File and I/O
File Descriptor Operations
Memory
Message Queues
Network Access
Process Control
Shared Memory
string
System-Wide
Time-Related""".split("\n")

type_dict = {}

for i in range(len(types)):
    type_dict[types[i]] = i

print(type_dict)
pickle.dump(type_dict, open("types.pickle", "wb"))


