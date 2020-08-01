import numpy as np
from typing import Union
from sklearn.base import ClassifierMixin, RegressorMixin

from .data import load_data
from .model import load_model, reg2clf_elbow_method


def model_predict(
    model: Union[ClassifierMixin, RegressorMixin], asm_vecs: np.array
) -> np.array:
    predicted_results = model.predict(asm_vecs)
    if isinstance(model, RegressorMixin):
        y_pred = reg2clf_elbow_method(predicted_results)
    else:
        y_pred = predicted_results
    return np.argwhere(y_pred == True).flatten()


def predict_chain(csvfile: str, model="Gaussian Process") -> list:
    X, y = load_data(csvfile, convert_label=False)
    try:
        model = load_model(f"{model}.pkl")
    except FileNotFoundError:
        raise RuntimeError("Model does not exist.")
    results = model_predict(model, X)
    return list(y[results])
