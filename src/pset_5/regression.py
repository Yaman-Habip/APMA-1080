import numpy as np
from scipy.stats import norm

X = [0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 1.00]
Y = [0.70, 8.20, 1.30, 5.30, 3.60, 3.50, 1.80, 6.70, 23.90, 20.80]

prob = 1
for x, y in zip(X, Y):
    prob *= norm.pdf(y, x * 20 - 3, 4)

print(-np.log(prob))
