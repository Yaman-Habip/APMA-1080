import numpy as np
from pset_2.pset_2 import MCSample
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


n_1 = 20
mu_1 = [0.5, 0, 0.5, 0, 0]
P_1 = [
    [0, 1, 0, 0, 0],
    [0.2, 0.0, 0.8, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1],
    [0.9, 0, 0.1, 0, 0],
]
C_1 = [[1, 0], [1, 0], [0, 1], [0, 1], [0, 1]]

for _ in range(5):
    print(HMMSample(C_1, P_1, mu_1, n_1)[1])
