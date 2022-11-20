import numpy as np
import matplotlib.pyplot as plt


N = 40

d1 = np.exp(-abs(np.random.randn(N) * 3))
d2 = np.exp(-abs(np.random.randn(N) * 5))
data_mean = [np.mean(d1), np.mean(d2)]

ds = np.zeros(N)
for i in range(N):
    ds[i] = np.sqrt((d1[i] - data_mean[0]) ** 2 + (d2[i] - data_mean[1]) ** 2)

ds = (ds - np.mean(ds)) / np.std(ds)

fig, ax = plt.subplots(1, 2, figsize=(8, 6))

ax[0].plot(d1, d2, 'ko', markerfacecolor='k')
ax[0].set_xticks([])
ax[0].set_yticks([])
ax[0].set_xlabel('Variable x')
ax[0].set_ylabel('Variable y')

ax[0].plot(data_mean[0], data_mean[1], 'kp', markerfacecolor='g', markersize=15)

ax[1].plot(ds, 'ko', markerfacecolor=[.7, .5, .3], markersize=12)
ax[1].set_xlabel('Data index')
ax[1].set_ylabel('Z distance')


distance_threshold = 2.5

outliers = np.where(ds > distance_threshold)[0]

ax[1].plot(outliers, ds[outliers], 'x', color='r', markersize=20)
ax[0].plot(d1[outliers], d2[outliers], 'x', color='r', markersize=20)

plt.show()
