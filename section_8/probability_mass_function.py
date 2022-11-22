import matplotlib.pyplot as plt
import numpy as np

N = 10004
data_1 = np.cumsum(np.sign(np.random.randn(N)))
data_2 = np.cumsum(np.sign(np.random.randn(N)))

plt.plot(np.arange(N), data_1, linewidth=2)
plt.plot(np.arange(N), data_2, linewidth=2)
plt.show()

n_bins = 50

y, x = np.histogram(data_1, n_bins)
x1 = (x[1:] + x[:-1]) / 2
y1 = y / sum(y)

y, x = np.histogram(data_2, n_bins)
x2 = (x[1:] + x[:-1]) / 2
y2 = y / sum(y)

plt.plot(x1, y1, x2, y2, linewidth=3)
plt.legend(('ts1', 'ts2'))
plt.xlabel('Data value')
plt.ylabel('Probability')
plt.show()
