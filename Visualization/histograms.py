import matplotlib.pyplot as plt
import numpy as np

n = 1000

# Log normal distribution
data = np.exp(np.random.randn(n)/2)
# plt.plot(data, 's')

k = 50

plt.hist(data, bins=k)

y, x = np.histogram(data, bins=k)

xx = (x[1:] + x[:-1]) / 2
plt.plot(xx, y)
plt.show()
