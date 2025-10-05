import numpy as np
from pset_2.mc_sample import MCSample
from tabulate import tabulate


def NoisySequence(Z, C):
    m = len(C[0])
    X = []
    for z in Z:
        X.append(np.random.choice(m, p=C[z - 1]) + 1)

    return X


def HMMSample(C, P, mu, n):
    hidden = MCSample(P, mu, n)
    return hidden, NoisySequence(hidden, C)
