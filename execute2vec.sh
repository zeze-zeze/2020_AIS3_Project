#!/bin/bash
python ./objconv/obj2asm.py $1 tmp_file_123123
python3 ./asm_to_vec.py tmp_file_123123 $2
rm tmp_file_123123
