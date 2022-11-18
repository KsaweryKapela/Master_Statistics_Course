import numpy as np

N = 10
data = np.log(np.random.rand(N))

data_min = min(data)
data_max = max(data)

data_scaled = (data - data_min) / (data_max - data_min)

data_unscaled = data_scaled * (data_max - data_min) + data_min

for num_1 in zip(data, data_scaled, data_unscaled):
    print(num_1)
