import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from statsmodels import robust

N = 400
data_1 = np.random.normal(1, 1, N)
data_2 = np.random.randn(N) ** 3

fig, ax = plt.subplots(2, 1, figsize=(8, 6))

ax[0].plot(data_1)
ax[1].plot(data_2)
plt.show()

z_data_1 = (data_1 - np.mean(data_1)) / np.std(data_1)
z_data_2 = (data_2 - np.mean(data_2)) / np.std(data_2)

z_MAD_1 = stats.norm.ppf(.75) * (data_1 - np.median(data_1)) / robust.mad(z_data_1)
z_MAD_2 = stats.norm.ppf(.75) * (data_2 - np.median(data_2)) / robust.mad(z_data_2)

fig_2, ax = plt.subplots(2, 2, figsize=(8, 6))
ax[0, 0].plot(z_data_1)
ax[0, 1].plot(z_data_2)

ax[1, 0].plot(z_MAD_1)
ax[1, 1].plot(z_MAD_2)
plt.show()
