import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

N = 100

data_1 = np.random.normal(loc=0, size=N)
data_2 = np.random.normal(loc=2, size=N)

data = pd.DataFrame({'data_1': data_1, 'data_2': data_2})
data = data.melt()
data['dummy'] = 0

sns.violinplot(data=data, y='value', split=True, hue='variable', x='dummy')

plt.show()
