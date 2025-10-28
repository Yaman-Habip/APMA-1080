import numpy as np
import matplotlib.pyplot as plt


def A(theta, n):
    return (0.5 - theta) ** 2


def B(theta, n):
    return (theta - theta**2) / n


def C(theta, n):
    return ((n * (theta - theta**2)) / (n + 2) ** 2) + (
        ((1 + theta * n) / (n + 2)) - theta
    ) ** 2


n = 5
theta = np.linspace(0, 1, 100)

a_values = [A(t, n) for t in theta]
b_values = [B(t, n) for t in theta]
c_values = [C(t, n) for t in theta]

plt.figure(figsize=(10, 6))
plt.plot(theta, a_values, label="A(θ, n=5)", linewidth=2)
plt.plot(theta, b_values, label="B(θ, n=5)", linewidth=2)
plt.plot(theta, c_values, label="C(θ, n=5)", linewidth=2)
plt.xlabel("θ")
plt.ylabel("MSE")
plt.title("Functions A, B, and C vs θ (n=5)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
