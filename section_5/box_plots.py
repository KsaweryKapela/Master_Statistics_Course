import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

rows = 30
columns = 6

data = np.zeros((rows, columns))

for index in range(columns):
    data[:, index] = 30 * np.random.randn(rows) * (2 * index / (columns - 1) - 1) ** 2 + (index + 1) ** 2

plt.boxplot(data)
plt.show()

sns.boxplot(data=data, orient='V')
plt.show()

df = pd.DataFrame(data, columns=['zero', 'one', 'two', 'three', 'four', 'five'])
sns.boxplot(data=df, orient='h')
plt.show()