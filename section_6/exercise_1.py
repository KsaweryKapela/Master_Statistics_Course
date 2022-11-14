# log-normal distrubution
import numpy as np
from matplotlib import pyplot as plt

fig, ax = plt.subplots(1, 4, figsize=(16, 4))

# small size/ small outlier

N1 = 100
bins1 = 20

data1 = np.random.randn(N1)
data1 = np.exp(data1)
data1 = np.append(data1, max(data1) ** 2)

median1 = np.median(data1)
mean1 = np.mean(data1)

y1, x1 = np.histogram(data1, bins1)
x1 = (x1[:-1] + x1[1:]) / 2

ax[0].plot(x1, y1)
ax[0].plot([mean1, mean1], [0, max(y1)], 'g--', label="Mean")
ax[0].plot([median1, median1], [0, max(y1)], 'r--', label="Median")
ax[0].title.set_text('small size & small outlier')
ax[0].legend()

# small size/ large outlier

N2 = 100
bins2 = 20

data2 = np.random.randn(N2)
data2 = np.exp(data2)
data2 = np.append(data2, max(data2) ** 6)

median2 = np.median(data2)
mean2 = np.mean(data2)

y2, x2 = np.histogram(data2, bins2)
x2 = (x2[:-1] + x2[1:]) / 2

ax[1].plot(x2, y2)
ax[1].plot([mean2, mean2], [0, max(y2)], 'g--', label="Mean")
ax[1].plot([median2, median2], [0, max(y2)], 'r--', label="Median")
ax[1].title.set_text('small size & large outlier')
ax[1].legend()

# large size/ small outlier

N3 = 1000
bins3 = 20

data3 = np.random.randn(N3)
data3 = np.exp(data3)
data3 = np.append(data3, max(data3) * 2)

median3 = np.median(data3)
mean3 = np.mean(data3)

y3, x3 = np.histogram(data3, bins3)
x3 = (x3[1:] + x3[:-1]) / 2

ax[2].plot(x3, y3)
ax[2].plot([mean3, mean3], [0, max(y3)], 'g--', label="Mean")
ax[2].plot([median3, median3], [0, max(y3)], 'r--', label="Median")
ax[2].title.set_text('large size & small outlier')
ax[2].legend()

# large size/ small outlier

N4 = 1000
bins4 = 20

data4 = np.random.randn(N4)
data4 = np.exp(data4)
data4 = np.append(data4, max(data4) ** 4)

median4 = np.median(data4)
mean4 = np.mean(data4)

y4, x4 = np.histogram(data4, bins4)
x4 = (x4[:-1] + x4[1:]) / 2

ax[3].plot(x4, y4)
ax[3].plot([mean4, mean4], [0, max(y4)], 'g--', label="Mean")
ax[3].plot([median4, median4], [0, max(y4)], 'r--', label="Median")
ax[3].title.set_text('large size & large outlier')
ax[3].legend()

plt.show()

