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

stds = np.zeros(3)

stds[0] = np.std(d1, ddof=1)
stds[1] = np.std(d2, ddof=1)
stds[2] = np.std(d3, ddof=1)

plt.plot(x1, y1, 'b', x2, y2, 'r', x3, y3, 'k')
plt.plot([mean_d1, mean_d1], [0, max(y1)], 'b--', [mean_d2, mean_d2], [0, max(y2)],
         'r--', [mean_d3, mean_d3], [0, max(y3)], 'y--')

plt.plot([mean_d1 - stds[0], mean_d1 + stds[0]], [0.4 * max(y1), 0.4 * max(y1)], 'b', linewidth=10)
plt.plot([mean_d2 - stds[1], mean_d2 + stds[1]], [0.5 * max(y2), 0.5 * max(y2)], 'r', linewidth=10)
plt.plot([mean_d3 - stds[2], mean_d3 + stds[2]], [0.6 * max(y3), 0.6 * max(y3)], 'k', linewidth=10)

plt.xlabel('Data values')
plt.ylabel('Data counts')

##############

variances = np.arange(1, 11)
N = 300

var_measures = np.zeros((4, len(variances)))

for i in range(len(variances)):
    data = np.random.randn(N) * variances[i]
    data_cent = data - np.mean(data)
    var_measures[0, i] = sum(data_cent ** 2) / (N - 1)
    var_measures[1, i] = sum(data_cent ** 2) / N
    var_measures[2, i] = np.sqrt(sum(data_cent ** 2) / (N - 1))
    var_measures[3, i] = sum(abs(data_cent)) / (N - 1)

plt.plot(variances, var_measures.T)
plt.legend(('Var', 'biased var', 'Std', 'MAD'))


data = np.random.poisson(3, 300)

fig, ax = plt.subplots(2, 1)
ax[0].plot(data, 's')
ax[0].set_title('Poisson noise')

ax[1].hist(data)

#############

lambdas = np.linspace(1, 12, 15)

fano = np.zeros(len(lambdas))
cv = np.zeros(len(lambdas))

for li in range(len(lambdas)):
    data = np.random.poisson(lambdas[li], 1000)

    cv[li] = np.std(data) / np.mean(data)
    fano[li] = np.var(data) / np.mean(data)

plt.plot(lambdas, cv, 'bs-')
plt.plot(lambdas, fano, 'ro-')
plt.legend(('CV', 'Fano'))
plt.xlabel('Lambda')
plt.ylabel('CV or Fano')

plt.show()
