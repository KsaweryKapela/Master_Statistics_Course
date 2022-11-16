import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import seaborn as sns

n = 1000

k = 40

data = np.exp(np.random.randn(n) / 2)

plt.hist(data, k)
plt.xlabel('Value')
plt.ylabel('Count')
plt.show()

r = 2 * stats.iqr(data) * n ** (-1 / 3)
k = np.ceil((max(data) - min(data)) / r)

plt.hist(data, int(k))

plt.xlabel('Value')
plt.ylabel('Count')
plt.title(f'F-D "rule" using {k} bins')
plt.show()

plt.hist(data, 'fd')
plt.show()

sns.histplot(data)
plt.show()

bins2try = np.round(np.linspace(5, n / 2, 30))

for bini in range(len(bins2try)):
    y, x = np.histogram(data, int(bins2try[bini]))
    x = (x[:-1] + x[1:]) / 2
    plt.plot(x, y, '.-')

plt.show()
