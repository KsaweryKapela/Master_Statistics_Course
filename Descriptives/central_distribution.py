import numpy as np
from matplotlib import pyplot as plt
import scipy.stats
from scipy import stats

N = 10001
n_bins = 30

d1 = np.random.randn(N) - 1
d2 = 3 * np.random.randn(N)
d3 = np.random.randn(N) + 1

y1, x1 = np.histogram(d1, n_bins)
x1 = (x1[1:] + x1[:-1]) / 2

y2, x2 = np.histogram(d2, n_bins)
x2 = (x2[1:] + x2[:-1]) / 2

y3, x3 = np.histogram(d3, n_bins)
x3 = (x3[1:] + x3[:-1]) / 2

plt.plot(x1, y1, 'b')
plt.plot(x2, y2, 'r')
plt.plot(x3, y3, 'k')

########

mean_d1 = np.mean(d1)
mean_d2 = np.mean(d2)
mean_d3 = np.mean(d3)

plt.plot([mean_d1, mean_d1], [0, max(y1)], 'b--')
plt.plot([mean_d2, mean_d2], [0, max(y2)], 'r--')
plt.plot([mean_d3, mean_d3], [0, max(y3)], 'k--')

########

d4 = np.hstack((np.random.randn(N) - 2, np.random.randn(N) + 2))
y4, x4 = np.histogram(d4, n_bins)
x4 = (x4[:-1] + x4[1:] / 2)

mean_d4 = np.mean(d4)

plt.plot(x4, y4, 'b')
plt.plot([mean_d4, mean_d4], [0, max(y4)], 'b--')


########

shift = 0
stretch = .7
n = 2000
nbins = 50

data = stretch * np.random.randn(n) + shift
data = np.exp(data)

y, x = np.histogram(data, nbins)
x = x[:-1] + x[1:] / 2

data_mean = np.mean(data)
data_median = np.median(data)

fig, ax = plt.subplots(2, 1, figsize=(4, 6))
ax[0].plot(data, '.', color=[.5, .5, .5], label='Data')
ax[0].plot([1, n], [data_mean, data_mean],  'r--', label='mean')
ax[0].plot([1, n], [data_median, data_median],  'b--', label='median')
ax[0].legend()

ax[1].plot(x, y)
ax[1].plot([data_mean, data_mean], [0, max(y)],  'y--', )
ax[1].plot([data_median, data_median], [0, max(y)],  'o--')
ax[1].legend()

plt.show()

######

data = np.round(np.random.randn(10))
print(data)

uniq_data = np.unique(data)
for i in range(len(uniq_data)):
    print(f'{uniq_data[i]} appears {sum(data==uniq_data[i])} times')

print(f'\nThe modal value is {stats.mode(data, keepdims=True)[0][0]}')