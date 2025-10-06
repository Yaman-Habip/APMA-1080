from itertools import product
from typing import Counter

import numpy as np

z_seqs = list(product([1, 2, 3], repeat=10))
x_seq = (2, 1, 1, 1, 2, 1, 2, 2, 1, 2)

mu = [0.3335, 0.3333, 0.3332]
P = [[0.2, 0.7, 0.1], [0.4, 0.0, 0.6], [0.0, 1.0, 0.0]]
C = [[0.9, 0.1], [0.2, 0.8], [0.5, 0.5]]

z_probs = []
for seq in z_seqs:
    prob = mu[seq[0] - 1]
    for i, z in enumerate(seq[1:]):
        prob *= P[seq[i] - 1][z - 1]
    z_probs.append(prob)

x_probs = []
for seq in z_seqs:
    prob = 1.0
    for i, x in enumerate(x_seq):
        prob *= C[seq[i] - 1][x - 1]
    x_probs.append(prob)

total_x_prob = sum(z * x for z, x in zip(z_probs, x_probs))
print(total_x_prob)
conditional_probs = [z * x for z, x in zip(z_probs, x_probs)]

cond_maximizer = np.argmax(conditional_probs)
print("Conditional Maximizer:", z_seqs[cond_maximizer])
print("Max sequence probability:", z_probs[cond_maximizer])
print(
    "Probability given X1:10:",
    z_probs[cond_maximizer] * x_probs[cond_maximizer] / total_x_prob,
)
