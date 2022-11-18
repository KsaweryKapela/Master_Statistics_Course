import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

data = np.random.poisson(3, 1000)**2

data_mean = np.mean(data)
data_std = np.std(data, ddof=1)

# =
# data_mean = data.mean()
# data_std  = data.std(ddof=1)


plt.plot(data, 's', markersize=3)
plt.xlabel('Data index')
plt.ylabel('Data value')
plt.title(f'Mean = {np.round(data_mean,2)}; std = {np.round(data_std,2)}')

plt.show()

data_z = (data-data_mean) / data_std

# =
# data_z = stats.zscore(data)

data_z_mean = np.mean(data_z)
data_z_std = np.std(data_z, ddof=1)

plt.plot(data_z, 's', markersize=3)
plt.xlabel('Data index')
plt.ylabel('Data value')
plt.title(f'Mean = {np.round(data_z_mean, 2)}; std = {np.round(data_z_std, 2)}')

plt.show()

plt.plot(data, data_z, 's')
plt.xlabel('Original')
plt.ylabel('Z-transformed')
plt.title('Correlation r = %g' % np.corrcoef(data, data_z)[0, 0])
plt.show()

