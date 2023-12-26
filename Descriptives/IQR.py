import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

n = 1000
data = np.random.randn(n)**2

dataR = stats.rankdata(data)/n
q1 = np.argmin((dataR-.25)**2)
q3 = np.argmin((dataR-.75)**2)

iq_vals = data[[q1, q3]]

iq_range1 = iq_vals[1] - iq_vals[0]

iq_range2 = stats.iqr(data)

print(iq_range1, iq_range2)
