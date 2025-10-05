import numpy as np
from tabulate import tabulate


def MCSample(P, miu, n):
    choices = list(range(1, len(miu) + 1))
    current = np.random.choice(choices, p=miu)
    states = [current]
    for _ in range(n - 1):
        current = np.random.choice(choices, p=P[current - 1])
        states.append(current)

    return states


transition = [[0.1, 0.8, 0.1, 0], [0, 0, 0.5, 0.5], [0, 0, 0, 1], [0.5, 0.2, 0.2, 0.1]]
probs = [0.25, 0.25, 0.25, 0.25]
iters = 10**5

result = MCSample(transition, probs, iters)

p_approx = np.zeros((4, 4))
_, counts = np.unique(result, return_counts=True)

for current in range(4):
    for next in range(4):
        p_approx[current][next] = (
            sum(
                1
                for i in range(iters - 1)
                if result[i] == current + 1 and result[i + 1] == next + 1
            )
            / counts[current]
        )

p_approx = np.round(p_approx, 4)

print(
    tabulate(
        p_approx,
        tablefmt="pretty",
        showindex=range(1, 5),
        headers=range(1, 5),
    )
)
