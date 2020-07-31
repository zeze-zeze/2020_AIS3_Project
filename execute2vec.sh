#!/bin/bash
python ./objconv/obj2asm.py $1 $2
python3 ./asm_to_vec.py $2 $3
rm $2
