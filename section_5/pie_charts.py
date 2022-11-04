import numpy as np
from matplotlib import pyplot as plt

n_bins = 5
total_n = 100

raw_data = np.ceil(np.logspace(np.log10(1/2), np.log10(n_bins-.01), total_n))


unique_values = np.unique(raw_data)
pie_data = np.zeros(len(unique_values))

for index in range(len(unique_values)):
    pie_data[index] = sum(raw_data == unique_values[index])

plt.pie(pie_data, labels=100 * pie_data / sum(pie_data))
plt.show()

plt.pie(pie_data, labels=['Zero', 'One', 'Two', 'Three', 'Four'])
plt.show()

# continuous data

data = np.exp(np.random.randn(50)/10)

histout = np.histogram(data, bins=5)
plt.pie(histout[0])
plt.show()
