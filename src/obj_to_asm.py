#!/usr/bin/env python
__author__ = "Bronson (@bronson113), Tomy Hsieh (@tomy0000000)"
__credits__ = ["Bronson", "Tomy Hsieh"]
__license__ = "MIT"

import os
import sys

TMP_FILE = "tmp123123.s"
OBJCONV_PATH = os.path.join(
    os.path.abspath(os.path.dirname(__file__)), "objconv/objconv"
)


def execute(input_file):
    os.system(f"{OBJCONV_PATH} -fnasm {input_file} {TMP_FILE} 1> /dev/null")
    f = "\n".join([i.split(";")[0] for i in open(TMP_FILE, "r").read().split("\n")])
    os.system(f"rm {TMP_FILE}")
    f = "\n".join([i for i in f.split("\n") if i != ""])
    f = "\n".join([i for i in f.split("\n") if "ALIGN" not in i])
    f = "\n".join([i for i in f.split("\n") if "extern" not in i])
    f = "\n".join([i for i in f.split("\n") if "default" not in i])
    f = "\n".join([i for i in f.split("\n") if "global" not in i])
    f = f.replace("?_0", ".L")
    f = f.replace("?_1", ".L1")
    f = f.replace(".L0", ".L")
    f = f.replace(".L0", ".L")
    f = f.replace(".L0", ".L")
    f = f.replace(".L0", ".L")
    f = "\n".join(
        [
            "\n".join(i.split("\n")[1:])
            for i in f.split("SECTION")
            if "noexecute" not in i and "plt" not in i
        ]
    )
    f = "fs:".join([i.replace(":", ":\n       ") for i in f.split("fs:")])
    return "\n".join([i for i in f.split("\n") if i.strip() != ""])


if __name__ == "__main__":
    if len(sys.argv) <= 2:
        sys.exit("Usage: ./obj2asm.py infile outfile")
    elif len(sys.argv) == 3:
        with open(sys.argv[2], "w") as f:
            output = execute(sys.argv[1])
            f.write(output)
    else:
        sys.exit("Too Many Arguments")
