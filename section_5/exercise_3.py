import numpy as np
from matplotlib import pyplot as plt

data_lin = np.linspace(start=0.001, stop=10, num=100)
data_log = np.exp(data_lin)

# linear scale
plt.plot(data_log[:40])
plt.plot(data_lin)
plt.show()

# log scale
plt.plot(data_log)
plt.plot(data_lin)
plt.yscale("log")
plt.show()
