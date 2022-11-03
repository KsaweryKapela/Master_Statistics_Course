import matplotlib.pyplot as plt
import numpy as np

n = 1000
data = np.exp(np.random.randn(n) / 2)

k = 40

plt.hist(data, bins=k)

counts, bin_edges = np.histogram(data, bins=k)

proportions = counts / np.sum(counts)
plt.hist(bin_edges[:-1], bin_edges, weights=proportions)

bin_centers = (bin_edges[1:] + bin_edges[:-1]) / 2
plt.plot(bin_centers, counts)
plt.show()

plt.plot(bin_centers, proportions)
plt.show()
