import csv

import numpy as np
import pandas as pd
from sklearn.datasets import make_classification


def load_data(filename: str, convert_label: bool = True) -> (np.ndarray, np.ndarray):
    df = pd.read_csv(filename, header=None)
    if convert_label:
        df[0] = df[0].apply(lambda x: int("evil" in x))
    data = df.to_numpy()
    return data[:, 1:], data[:, 0]


def dump_data(filename: str, X: np.ndarray, y: np.ndarray) -> None:
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        for vec, label in zip(X, y):
            writer.writerow([int(label)] + vec.tolist())


def generate_data(
    n_samples: int = 100, n_features: int = 310
) -> (np.ndarray, np.ndarray):
    X, y = make_classification(
        n_samples=n_samples,
        n_features=n_features,
        n_informative=2,
        n_redundant=0,
        n_clusters_per_class=1,
        random_state=1,
    )
    X += 2 * np.random.RandomState(2).uniform(size=X.shape)
    return X, y
