import numpy as np
from matplotlib import pyplot as plt

averages = np.zeros(100 * 100)

for i in range(1, 101):
    for ii in range(1, 101):
        averages[(i - 1) * 100 + (ii - 1)] = (i + ii) / 2

sample_size = 500
sample = np.random.choice(averages, sample_size)

plt.hist(sample, 20)
plt.show()
