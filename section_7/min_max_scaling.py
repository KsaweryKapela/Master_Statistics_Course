import matplotlib.pyplot as plt
import numpy as np

N = 42
data = np.log(np.random.rand(N)) * 234 + 934

dataMin = min(data)
dataMax = max(data)

dataS = (data - dataMin) / (dataMax - dataMin)

fig, ax = plt.subplots(1, 2, figsize=(8, 4))
ax[0].plot(1 + np.random.randn(N) / 20, data, 'ks')
ax[0].set_xlim([0, 2])
ax[0].set_xticks([])
ax[0].set_ylabel('Original data scale')
ax[0].set_title('Original data')

ax[1].plot(1 + np.random.randn(N) / 20, dataS, 'ks')
ax[1].set_xlim([0, 2])
ax[1].set_xticks([])
ax[1].set_ylabel('Unity-normed data scale')
ax[1].set_title('Scaled data')

plt.show()

plt.plot(data, dataS, 'ks')
plt.xlabel('Original')
plt.ylabel('Scaled')
plt.show()

#################

newMin = 4
newMax = 8.7

dataSS = dataS * (newMax - newMin) + newMin

print([min(dataSS), max(dataSS)])
