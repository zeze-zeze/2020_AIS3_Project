import os
import pickle
import numpy as np
from typing import Union
from sklearn.base import ClassifierMixin, RegressorMixin

FILE_DIR = os.path.abspath(os.path.dirname(__file__))
MODEL_DIR = os.path.join(FILE_DIR, "models")


def list_models() -> list:
    models = []
    for file in os.listdir(MODEL_DIR):
        full_path = os.path.join(FILE_DIR, "models", file)
        if os.path.isfile(full_path) and file.endswith(".pkl"):
            models.append(file.replace(".pkl", ""))
    return models


def load_model(filename: str) -> Union[ClassifierMixin, RegressorMixin]:
    path = os.path.join(MODEL_DIR, filename)
    with open(path, "rb") as file:
        model = pickle.load(file)
    return model


def dump_model(model: Union[ClassifierMixin, RegressorMixin], filename: str) -> None:
    path = os.path.join(MODEL_DIR, filename)
    with open(path, "wb") as file:
        pickle.dump(model, file)


def reg2clf_elbow_method(y_pred: np.ndarray) -> np.ndarray:
    indexed = np.array(list(zip(np.arange(len(y_pred)), y_pred)))
    values_sort = indexed[indexed[:, 1].argsort()]
    value_diff = np.diff(values_sort[:, 1])
    high_pass = values_sort[np.argmax(value_diff)][1]
    return y_pred > high_pass
