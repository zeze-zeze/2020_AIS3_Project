#!/usr/bin/env python
__author__ = "Tomy Hsieh (@tomy0000000)"
__credits__ = ["Tomy Hsieh"]
__license__ = "MIT"

import os

from art.random_c import main as random_c


def main():

    WORKDIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "tmp"))
    TMP_SOURCE = os.path.join(WORKDIR, "tmp.c")
    TMP_BIN = os.path.join(WORKDIR, "tmp.bin")

    # Generate Working Directory
    if not os.path.exists(WORKDIR):
        os.mkdir(WORKDIR)

    # Generating Source Code
    c_source = random_c()
    with open(TMP_SOURCE, "w") as file:
        file.write(c_source)

    # Compiling
    os.system(f"gcc {TMP_SOURCE} -o {TMP_BIN}")


if __name__ == "__main__":
    main()
