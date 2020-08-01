#!/usr/bin/env python
__author__ = "Bronson (@bronson113), Tomy Hsieh (@tomy0000000)"
__credits__ = ["Bronson", "Tomy Hsieh"]
__license__ = "MIT"

import os
import sys

import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "asm2vec")))
print(sys.path)

import asm2vec.asm
import asm2vec.model
import asm2vec.parse

MODEL_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), "asm2vec.model")


def cosine_similarity(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))


def model_deserialization(s):

    tmp = eval(s)
    model = asm2vec.model.Asm2Vec(d=200)
    tmp3 = asm2vec.internal.training.Asm2VecParams()
    tmp3.populate(tmp["params"])

    tmp4 = []
    for k, v in tmp["vocab"].items():
        tmpv = dict(
            [
                (k.encode(), v2.encode()) if type(v2) == str else (k.encode(), v2)
                for k, v2 in v.items()
            ]
        )
        tmp5 = asm2vec.repo._deserialize_token(tmpv)
        tmp4.append((k, tmp5))
    tmp2 = asm2vec.model.Asm2VecMemento()
    tmp2.params = tmp3
    tmp2.vocab = dict(tmp4)
    model.set_memento(tmp2)

    return model


def training():
    training_funcs = asm2vec.parse.parse("out_onlockdown_5.s", func_names=["main"])

    print("# of training functions:", len(training_funcs))

    model = asm2vec.model.Asm2Vec(d=200)
    training_repo = model.make_function_repo(training_funcs)
    model.train(training_repo)
    print("Training complete.")

    for tf in training_repo.funcs():
        print(
            'Norm of trained function "{}" = {}'.format(
                tf.sequential().name(), np.linalg.norm(tf.v)
            )
        )

    s = asm2vec.repo.serialize_vocabulary(model.memento().vocab)

    with open(MODEL_PATH, "w") as f:
        f.write(repr(model.memento().serialize()))


def vectorizer(fname, oname):
    estimating_funcs = asm2vec.parse.parse(fname, func_names=["main"])

    model = model_deserialization(open(MODEL_PATH, "r").read())

    # print(list(model.to_vec(estimating_funcs[0])))
    estimating_funcs_vec = []
    for func in estimating_funcs:
        print(func.name())
        estimating_funcs_vec.append(model.to_vec(func))

    #    for (ef, efv) in zip(estimating_funcs, estimating_funcs_vec):
    #        print(ef.name()+','+str(list(efv)))
    with open(oname, "w") as f:
        # f.write('function_name,vector\n')
        for (ef, efv) in zip(estimating_funcs, estimating_funcs_vec):
            f.write(ef.name() + ", " + str(list(efv))[1:-1] + "\n")


if __name__ == "__main__":
    # training()
    vectorizer(sys.argv[1], sys.argv[2])
