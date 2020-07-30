#!/usr/bin/env python
import csv

reader = csv.reader(open('libtype.csv'))
func_dict = {}
for row in reader:
    func_dict[row[0]] = row[1]

print(func_dict)
