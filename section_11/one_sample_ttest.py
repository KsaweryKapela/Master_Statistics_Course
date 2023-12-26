import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

N = 20
population_mean = 0.5
data = np.random.randn(N) + population_mean

plt.plot(data, 'ko-', markerfacecolor='w', markersize=10)
plt.xlabel('Data index')
plt.ylabel('Data value')
plt.show()

h0_value = 0

t_numerator = np.mean(data) - h0_value
t_denominator = np.std(data, ddof=1) / np.sqrt(N)
t_value = t_numerator / t_denominator

degrees_of_freedom = N - 1

p_value = (1 - stats.t.cdf(abs(t_value), degrees_of_freedom)) * 2

x = np.linspace(-4, 4, 1001)
t_distribution = stats.t.pdf(x, degrees_of_freedom) * np.mean(np.diff(x))

plt.plot(x, t_distribution, linewidth=2)
plt.plot([t_value, t_value], [0, max(t_distribution)], 'r--')
plt.legend(('H_0 distribution', 'Observed t-value'))
plt.xlabel('t-value')
plt.ylabel('pdf(t)')
plt.title(f't({degrees_of_freedom}) = {t_value}, p={p_value}')


# PYTHON FUNCTION

t, p = stats.ttest_1samp(data, h0_value)
print(t, p)

plt.show()
