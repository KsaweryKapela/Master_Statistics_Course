import matplotlib.pyplot as plt
import numpy as np

N = 1000
numbers = np.ceil(8 * np.random.rand(N) ** 2)
numbers[numbers == 7] = 4
plt.plot(numbers, 'o')

N = 1000
numbers = np.ceil(8 * np.random.rand(N) ** 2)

u = np.unique(numbers)
probs = np.zeros(len(u))

for ui in range(len(u)):
    probs[ui] = sum(numbers == u[ui]) / N

entropee = -sum(probs * np.log2(probs + np.finfo(float).eps))

plt.bar(u, probs)
plt.title('Entropy = %g' % entropee)
plt.xlabel('Data value')
plt.ylabel('Probability')
plt.show()

N = 1123
brown_noise = np.cumsum(np.sign(np.random.randn(N)))

fig, ax = plt.subplots(2, 1, figsize=(4, 6))
ax[0].plot(brown_noise)
ax[0].set_xlabel('Data index')
ax[0].set_ylabel('Data value')
ax[0].set_title('Brownian noise')

ax[1].hist(brown_noise, 30)
ax[1].set_xlabel('Data value')
ax[1].set_ylabel('Counts')
plt.show()

n_bins = 50

nPerBin, bins = np.histogram(brown_noise, n_bins)
probs = nPerBin / sum(nPerBin)

entro = -sum(probs * np.log2(probs + np.finfo(float).eps))

print('Entropy = %g' % entro)
