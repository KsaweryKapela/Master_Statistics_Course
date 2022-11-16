import numpy as np
from matplotlib import pyplot as plt

np.random.seed(42)

N = 1123
brown_noise = np.cumsum(np.sign(np.random.randn(N)))

n_bins = list(range(4, 51))
entros = list()

for n in n_bins:
    nPerBin, bins = np.histogram(brown_noise, n)
    probs = nPerBin / sum(nPerBin)
    entro = -sum(probs * np.log2(probs + np.finfo(float).eps))
    entros.append(entro)

plt.figure(figsize=(12, 8))
plt.plot(n_bins,
         entros)
plt.xticks(range(0, 51, 5))
plt.xlabel('Number of bins')
plt.ylabel('Entropy')
plt.show()
