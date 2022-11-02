import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

rows = 30
columns = 6

##

data = np.zeros((rows, columns))


for index in range(columns):
    data[:, index] = 30 * np.random.randn(rows) * (2 * index / (columns - 1) - 1) ** 2 + (index + 1) ** 2


fig, ax = plt.subplots(1, 3, figsize=(8, 2))

ax[0].bar(range(columns), np.mean(data, axis=0))
ax[0].set_title('Bar plot')

ax[1].errorbar(range(columns), np.mean(data, axis=0), np.std(data, axis=0, ddof=1), marker='s', linestyle='')
ax[1].set_title('Errorbar plot')

ax[2].bar(range(columns), np.mean(data, axis=0))
ax[2].errorbar(range(columns), np.mean(data, axis=0), np.std(data, axis=0, ddof=1), marker='.', linestyle='', color='black')
plt.show()

##

xcrossings = [1, 2, 4, 5, 6, 9]
plt.bar(xcrossings, np.mean(data, axis=0))
plt.xticks(xcrossings)
plt.errorbar(xcrossings, np.mean(data, axis=0), np.std(data, axis=0, ddof=1), marker='.', linestyle='', color='black')
plt.title('Bar + errorplot')
plt.show()

##

data = [[2, 5, 4, 3], [1, 1, 8, 6]]
fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(8, 8))

ax[0, 0].imshow(data)

df = pd.DataFrame(data, columns=['prop 0', 'prop 1', 'prop 2', 'prop 3'])
df.plot(ax=ax[1, 0], kind='bar')
ax[1, 0].set_title('Grouping by rows')

ax[0, 1].imshow(np.array(data).T)

df.T.plot(ax=ax[1, 1], kind='bar')
ax[1, 1].set_title('Grouping by columns')

plt.show()
