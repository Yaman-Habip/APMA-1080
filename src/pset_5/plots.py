import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 1000)
comp1 = (
    (1 / 5)
    * (1 / np.sqrt(2 * np.pi * (1 / 9)))
    * np.exp(-((x + 2) ** 2) / (2 * (1 / 9)))
)
comp2 = (3 / 5) * (1 / np.sqrt(2 * np.pi)) * np.exp(-(x**2) / 2)
comp3 = (
    (1 / 5)
    * (1 / np.sqrt(2 * np.pi * (1 / 9)))
    * np.exp(-((x - 2) ** 2) / (2 * (1 / 9)))
)
pdf_gmm = comp1 + comp2 + comp3

plt.figure(figsize=(10, 6))
plt.plot(x, pdf_gmm, "k", linewidth=2, label="Combined PDF")
plt.xlabel("x")
plt.ylabel("Probability Density")
plt.grid(True)
plt.show()
