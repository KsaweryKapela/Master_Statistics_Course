import numpy as np
from matplotlib import pyplot as plt

a = np.zeros([10, 11])
print(a)
M = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
for i, m in enumerate(M):
    for j, n in enumerate(N):
        a[i][j] = 1 / (1 + m / n)
plt.imshow(a, cmap='hot', origin='lower')
plt.show()
