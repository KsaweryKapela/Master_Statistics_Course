import numpy as np
import matplotlib.pyplot as plt
from statsmodels import robust
import scipy.stats as stats

N = 40
data = np.random.randn(N)
data[data < -1] = data[data < -1] + 2
data[data > 2] = data[data > 2] ** 2
data = data * 200 + 50

data_z = (data - np.mean(data)) / np.std(data)

z_threshold = 3

fig, ax = plt.subplots(2, 1, figsize=(8, 6))

ax[0].plot(data, 'k^', markerfacecolor='w', markersize=12)
ax[0].set_xticks([])
ax[0].set_xlabel('Data index')
ax[0].set_ylabel('Orig. scale')

ax[1].plot(data_z, 'k^', markerfacecolor='w', markersize=12)
ax[1].plot([0, N], [z_threshold, z_threshold], 'r--')
ax[1].set_xlabel('Data index')
ax[1].set_ylabel('Z distance')
plt.show()


######

outliers = np.where(abs(data_z) > z_threshold)[0]
ax[0].plot(outliers, data[outliers], 'x', color='r', markersize=20)
ax[1].plot(outliers, data_z[outliers], 'x', color='r', markersize=20)
#######

z_threshold = 2
data_z = (data - np.mean(data)) / np.std(data)

color_z = 'brkm'
iterations = 0

while True:
    data_mean = np.nanmean(data_z)
    data_std = np.nanstd(data_z)
    data_z = (data_z - data_mean) / data_std

    to_remove = data_z > z_threshold
    if sum(to_remove) == 0:
        break
    else:
        plt.plot(np.where(to_remove)[0], data_z[to_remove], '%sx' % color_z[iterations], markersize=12)
        data_z[to_remove] = np.nan

    plt.plot(data_z, 'k^', markersize=12, markerfacecolor=color_z[iterations], label='iteration %g' % iterations)
    iterations += 1

plt.xticks([])
plt.ylabel('Z-score')
plt.xlabel('Data index')
plt.legend()
plt.show()

remove_from_data = np.where(np.isnan(data_z))[0]
print(remove_from_data)

#######

data_median = np.median(data)
data_MAD = robust.mad(data)
# MAD = median absolute deviation

data_modified_z = stats.norm.ppf(.75) * (data - data_median) / data_MAD

fig, ax = plt.subplots(2, 1, figsize=(8, 6))

ax[0].plot(data, 'k^', markerfacecolor='w', markersize=12)
ax[0].set_xticks([])
ax[0].set_xlabel('Data index')
ax[0].set_ylabel('Orig. scale')

ax[1].plot(data_modified_z, 'k^', markerfacecolor='w', markersize=12)
ax[1].plot([0, N], [z_threshold, z_threshold], 'r--')
ax[1].set_xlabel('Data index')
ax[1].set_ylabel('Median dev. units (Mz)')
plt.show()

