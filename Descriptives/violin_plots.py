import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import seaborn as sns

n = 1000
thresh = 5

data = np.exp(np.random.randn(n))
data[data > thresh] = thresh + np.random.randn(sum(data > thresh)) * 0.1

plt.hist(data, 30)
plt.title('Histogram')
plt.show()

plt.violinplot(data)
plt.title('Violin')
plt.show()

sns.swarmplot(data, orient='v')
plt.show()
