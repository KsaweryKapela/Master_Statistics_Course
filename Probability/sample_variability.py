import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

population = np.linspace(-5, 5, 10101)
normal_distribution = stats.norm.pdf(population)

n_samples = 40
sample_data = np.zeros(n_samples)

for sample in range(n_samples):
    sample_data[sample] = np.random.randn()

plt.hist(sample_data, density=True)
plt.plot(population, normal_distribution, 'r', linewidth=3)
plt.xlabel('Data values')
plt.ylabel('Probability')
plt.show()

population_n = 1000000
population = np.random.randn(population_n)
population = population - np.mean(population)

sample_size = 30

sample = np.random.randint(0, population_n, sample_size)
sample_mean = np.mean(population[sample])

sample_sizes = np.arange(30, 1000)

sample_means = np.zeros(len(sample_sizes))

for s in range(len(sample_sizes)):
    sample = np.random.randint(0, population_n, sample_sizes[s])
    sample_means[s] = np.mean(population[sample])

plt.plot(sample_sizes, sample_means, 's-')
plt.plot(sample_sizes[[0, -1]], [np.mean(population), np.mean(population)], 'r', linewidth=3)
plt.xlabel('sample size')
plt.ylabel('mean value')
plt.legend(('Sample means', 'Population mean'))
plt.show()
