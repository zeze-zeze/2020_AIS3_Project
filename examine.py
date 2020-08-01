import argparse
import os
import sys

from src.asm_to_vec import vectorizer as asm_to_vec
from src.obj_to_asm import execute as obj_to_asm
from src.classifying.model import list_models
from src.classifying.util import predict_chain as predict

WORKDIR = "tmp"
TMP_ASM = os.path.join(WORKDIR, "tmp.asm")
TMP_CSV = os.path.join(WORKDIR, "tmp.csv")


def main():
    parser = argparse.ArgumentParser(
        description="Check if binary include any evil function"
    )
    parser.add_argument(
        "-b", "--binary", type=str, required=True, help="dataset statistic report"
    )
    parser.add_argument(
        "-m", "--model", default="Gaussian Process", type=str, choices=list_models()
    )
    arg = parser.parse_args()

    # Convert to ASM
    asm = obj_to_asm(arg.binary)
    with open(TMP_ASM, "w") as file:
        file.write(asm)

    # Convert to Vectors
    asm_to_vec(TMP_ASM, TMP_CSV)

    # Predict
    results = predict(TMP_CSV, arg.model)
    for func in results:
        print(f"Target Function Found: {func}")


if __name__ == "__main__":
    main()
