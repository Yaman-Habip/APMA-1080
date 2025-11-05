from math import pi


with open("src/pset_7/Dataset1.txt", "r") as f:
    data = [[float(value) for value in line.split()] for line in f.readlines()]

pi_counts = [0, 0]
for row in data:
    pi_counts[int(row[0]) - 1] += 1

mu_sums = [0.0, 0.0]
for row in data:
    mu_sums[int(row[0]) - 1] += row[1]

print("MLE mu_1:", mu_sums[0] / pi_counts[0])
print("MLE mu_2:", mu_sums[1] / pi_counts[1])

mu_estimates = [mu_sums[0] / pi_counts[0], mu_sums[1] / pi_counts[1]]
variance_sums = [0.0, 0.0]
for row in data:
    variance_sums[int(row[0]) - 1] += (row[1] - mu_estimates[int(row[0]) - 1]) ** 2

print("MLE sigma_1:", (variance_sums[0] / pi_counts[0]) ** 0.5)
print("MLE sigma_2:", (variance_sums[1] / pi_counts[1]) ** 0.5)
