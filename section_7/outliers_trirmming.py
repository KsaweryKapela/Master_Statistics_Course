import numpy as np
import matplotlib.pyplot as plt

N = 40
data = np.random.randn(N)
data[data < -2] = -data[data < -2] ** 2
data[data > 2] = data[data > 2] ** 2

mean_centered_data = data - np.mean(data)

fig, ax = plt.subplots(1, 1)
ax.plot(data, 'k^', markerfacecolor='y', markersize=12)
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlabel('Data index')
ax.set_ylabel('Data value')


# option 1: remove k% of the data

percentile_threshold = 5

data_cutoff = np.percentile(abs(mean_centered_data), 100 - percentile_threshold)

outlier = np.where(abs(mean_centered_data) > data_cutoff)[0]
print(outlier)
ax.plot(outlier, data[outlier], 'rx', markersize=15)

# option 2: remove k most extreme values

values_number_threshold = 3  # number of values to delete

sorted_data = np.argsort(abs(mean_centered_data), axis=0)[::-1]

outliers = np.squeeze(sorted_data[:values_number_threshold])

ax.plot(outliers, data[outliers], 'go', markersize=15, alpha=.5)

ax.legend(('All data', '%g%% threshold' % (100 - percentile_threshold), '%g-value threshold' % values_number_threshold))

plt.show()

