import numpy as np
from matplotlib import pyplot as plt

n = 100

data_1 = np.random.randn(n)
data_2 = np.random.rand(n)

fig, ax = plt.subplots(1, 2, figsize=(8, 2))

ax[0].boxplot(data_1)
ax[1].boxplot(data_2)
plt.show()
