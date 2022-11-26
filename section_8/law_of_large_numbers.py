import matplotlib.pyplot as plt
import numpy as np

f1 = 2 / 8
f2 = 2 / 8
f3 = 1 / 8
f4 = 1 / 8
f5 = 1 / 8
f6 = 1 / 8

print(f1 + f2 + f3 + f4 + f5 + f6)

exp_value = 1 * f1 + 2 * f2 + 3 * f3 + 4 * f4 + 5 * f5 + 6 * f6

population = [1, 1, 2, 2, 3, 4, 5, 6]
for i in range(20):
    population = np.hstack((population, population))

n_population = len(population)

sample = np.random.choice(population, 8)

k = 5000
sampleAve = np.zeros(k)

for i in range(k):
    idx = np.floor(np.random.rand(i + 1) * n_population)
    sampleAve[i] = np.mean(population[idx.astype(int)])

plt.plot(sampleAve, 'k')
plt.plot([1, k], [exp_value, exp_value], 'r', linewidth=4)
plt.xlabel('Number of samples')
plt.ylabel('Value')
plt.ylim([exp_value - 1, exp_value + 1])
plt.legend(('Sample average', 'expected value'))

print(np.mean(sampleAve))
print(np.mean(sampleAve[:9]))

populationN = 1000000
population = np.random.randn(populationN)
population = population - np.mean(population)

sample_size = 30
number_of_exps = 500
sample_means = np.zeros(number_of_exps)

for expi in range(number_of_exps):
    sample_idx = np.random.randint(0, populationN, sample_size)
    sample_means[expi] = np.mean(population[sample_idx])

fig, ax = plt.subplots(2, 1, figsize=(4, 6))
ax[0].plot(sample_means, 's-')
ax[0].plot([0, number_of_exps], [np.mean(population), np.mean(population)], 'r', linewidth=3)
ax[0].set_xlabel('Experiment number')
ax[0].set_ylabel('mean value')
ax[0].legend(('Sample means', 'Population mean'))

ax[1].plot(np.cumsum(sample_means) / np.arange(1, number_of_exps + 1), 's-')
ax[1].plot([0, number_of_exps], [np.mean(population), np.mean(population)], 'r', linewidth=3)
ax[1].set_xlabel('Experiment number')
ax[1].set_ylabel('mean value')
ax[1].legend(('Sample means', 'Population mean'))

plt.show()

plt.hist(sample_means, 30)
plt.xlabel('Sample mean value')
plt.ylabel('Count')
plt.show()
