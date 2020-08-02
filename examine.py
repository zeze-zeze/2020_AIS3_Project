#!/usr/bin/env python
__author__ = "Tomy Hsieh (@tomy0000000)"
__credits__ = ["Tomy Hsieh"]
__license__ = "MIT"

import argparse
import os
import sys

from art.asm_to_vec import vectorizer as asm_to_vec
from art.obj_to_asm import execute as obj_to_asm
from art.classifying.model import list_models
from art.classifying.util import predict_chain as predict

WORKDIR = "tmp"
TMP_ASM = os.path.join(WORKDIR, "tmp.asm")
TMP_CSV = os.path.join(WORKDIR, "tmp.csv")


def main(args=sys.argv[1:]):
    parser = argparse.ArgumentParser(
        description="Check if executable binary include any evil function"
    )
    parser.add_argument(
        "-l",
        "--list",
        default=False,
        action="store_false",
        help="list all available model",
    )
    parser.add_argument(
        "-b",
        "--binary",
        type=str,
        nargs=1,
        required=True,
        help="the path to executable binary",
        metavar="executable_path",
    )
    parser.add_argument(
        "-m",
        "--model",
        default="Gaussian Process",
        type=str,
        nargs=1,
        choices=list_models(),
        help="the model used to classify function (default: Gaussian Process)",
        metavar="model_name",
    )
    arg = parser.parse_args(args=args)

    if arg.list:
        print(list_models())
        return 0

    full_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), arg.binary[0])
    if not os.path.isfile(full_path):
        raise FileNotFoundError(arg.binary[0])

    # Convert to ASM
    asm = obj_to_asm(full_path)
    with open(TMP_ASM, "w") as file:
        file.write(asm)

    # Convert to Vectors
    functions = asm_to_vec(TMP_ASM, TMP_CSV)
    print("Complete Function List: ")
    print(functions)

    # Predict
    results = predict(TMP_CSV, arg.model)
    for func in results:
        print(f"Target Function Found: {func}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
