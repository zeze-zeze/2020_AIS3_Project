#!/usr/bin/env python
__author__ = "Tomy Hsieh (@tomy0000000)"
__credits__ = ["Tomy Hsieh"]
__license__ = "MIT"

import os

# from src.asm_to_vec import vectorizer as asm_to_vec
# from src.obj_to_asm import execute as obj_to_asm
from src.random_c import main as random_c

WORKDIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "tmp"))
TMP_SOURCE = os.path.join(WORKDIR, "tmp.c")
TMP_BIN = os.path.join(WORKDIR, "tmp.bin")
# TMP_ASM = os.path.join(WORKDIR, "tmp.asm")
# EXPORT_CSV = os.path.join(WORKDIR, "vec.csv")

# Generate Working Directory
if not os.path.exists(WORKDIR):
    os.mkdir(WORKDIR)

# Generating Source Code
c_source = random_c()
with open(TMP_SOURCE, "w") as file:
    file.write(c_source)

# Compiling
os.system(f"gcc {TMP_SOURCE} -o {TMP_BIN}")

# # tmp.out -> tmp.s -> tmp.asm
# asm = obj_to_asm(TMP_BIN)
# with open(TMP_ASM, "w") as file:
#     file.write(asm)

# # tmp.asm -> vec.csv
# asm_to_vec(TMP_ASM, EXPORT_CSV)
