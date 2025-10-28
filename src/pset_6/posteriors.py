import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import beta

np.random.seed(43)

n = 2**20
x = np.random.random(n) < 0.6
MAX_N = 10


def beta_series(a, b):
    points = np.linspace(0, 1, 1000)
    return beta.pdf(points, a, b)


prior_pdf = beta_series(1, 1)
posterior_pdfs = []
for i in range(MAX_N):
    data = x[: 2**i]
    posterior_pdfs.append(beta_series(1 + sum(data), 1 + len(data) - np.sum(data)))


theta = np.linspace(0, 1, 1000)
plt.figure(figsize=(10, 6))
plt.plot(theta, prior_pdf, label="prior", linewidth=2)
for i, posterior in enumerate(posterior_pdfs):
    plt.plot(theta, posterior, label=f"n = 2^{i}", linewidth=2)
plt.xlabel("θ")
plt.ylabel("Probability Density")
plt.title("Prior and Posterior Distributions")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
