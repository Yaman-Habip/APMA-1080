import numpy as np


def MCSample(P, miu, n):
    choices = list(range(1, len(miu) + 1))
    current = np.random.choice(choices, p=miu)
    states = [current]
    for _ in range(n - 1):
        current = np.random.choice(choices, p=P[current - 1])
        states.append(current)

    return states
