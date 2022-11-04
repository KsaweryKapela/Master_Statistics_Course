import numpy as np
from matplotlib import pyplot as plt

n = 1000

data_1 = np.exp(np.random.randn(n)/2)
data_2 = np.exp(np.random.randn(n)/10)
data_3 = np.exp(np.random.randn(n)/2 + 1)

k = 5

y1, x1 = np.histogram(data_1, bins=k)
xx1 = (x1[0:-1] + x1[1:]) / 2
y1 = 100 * y1 / sum(y1)

y2, x2 = np.histogram(data_2, bins=k)
xx2 = (x2[0:-1] + x2[1:]) / 2
y2 = 100 * y2 / sum(y2)

y3, x3 = np.histogram(data_3, bins=k)
xx3 = (x3[0:-1] + x3[1:]) / 2
y3 = 100 * y3 / sum(y3)

plt.plot(xx1, y1, 's-', label='data1')
plt.plot(xx2, y2, 'o-', label='data2')
plt.plot(xx3, y3, '^-', label='data3')

plt.legend()
plt.xlabel('value')
plt.ylabel('probability')
plt.show()
