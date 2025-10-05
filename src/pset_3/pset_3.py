from pset_3.noisy_sequence import HMMSample

with open("X.txt", "r") as file:
    X = file.read()


P = [
    [0.3127, 0.1815, 0.2636, 0.2422],
    [0.3354, 0.2777, 0.0561, 0.3308],
    [0.2721, 0.2233, 0.2775, 0.2271],
    [0.2027, 0.2171, 0.2672, 0.3130],
]
miu = [0.2781, 0.2221, 0.2216, 0.2782]

from pset_2.pset_2 import MCSample as markov

Y = "".join(map(str, markov(P, miu, 10**5)))

x_freq = X.count("ACGT") / (len(X) - 2)
y_freq = Y.count("1234") / (len(Y) - 2)

print(f"P(X=ACGT) = {x_freq}")
print(f"P(Y=1234) = {y_freq}")
print(f"Ratio = {x_freq/y_freq}")


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
