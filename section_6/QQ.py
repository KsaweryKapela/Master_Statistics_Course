import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

n = 1000
data = np.random.randn(n)
# data = np.exp( np.random.randn(n)*.8 ) # log-norm distribution

x = np.linspace(-4, 4, 10001)
theo_norm = stats.norm.pdf(x)
theo_norm = theo_norm / max(theo_norm)

yy, xx = np.histogram(data, 40)
yy = yy / max(yy)
xx = (xx[:-1] + xx[1:]) / 2

plt.plot(xx, yy, label='Empirical')
plt.plot(x, theo_norm, label='Theoretical')
plt.legend()
plt.show()

zSortData = np.sort(stats.zscore(data))
sortNormal = stats.norm.ppf(np.linspace(0, 1, n))
plt.show()

plt.plot(sortNormal, zSortData, 'o')

xL, xR = plt.xlim()
yL, yR = plt.ylim()
lims = [np.min([xL, xR, yL, yR]), np.max([xL, xR, yL, yR])]
plt.xlim(lims)
plt.ylim(lims)

plt.plot(lims, lims)

plt.xlabel('Theoretical normal')
plt.ylabel('Observed data')
plt.title('QQ plot')
plt.axis('square')
plt.show()

x = stats.probplot(data, plot=plt)
