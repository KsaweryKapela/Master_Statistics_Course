import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

N = 1001
x = np.linspace(-4, 4, N)

gaus_dist = stats.norm.pdf(x)

plt.plot(x, gaus_dist)
plt.title('Analytic Gaussian distribution')
plt.show()

###################

stretch = 1  # variance
shift = 5  # mean
n = 1000

data = stretch*np.random.randn(n) + shift

plt.hist(data, 25)
plt.title('Empirical normal distribution')
plt.show()

###################

stretch = 2
shift = .5
n = 10000

data = stretch*np.random.rand(n) + shift/stretch/2
fig, ax = plt.subplots(2, 1, figsize=(5, 6))

ax[0].plot(data, '.', markersize=1)
ax[0].set_title('Uniform data values')

ax[1].hist(data, 25)
ax[1].set_title('Uniform data histogram')

plt.show()
###################

N = 1001
x = np.linspace(0, 10, N)
lognormdist = stats.lognorm.pdf(x, 1)

plt.plot(x, lognormdist)
plt.title('Analytic log-normal distribution')
plt.show()

###################

shift = 5
stretch = .5
n = 2000

data = stretch * np.random.randn(n) + shift
data = np.exp(data)

fig, ax = plt.subplots(2, 1, figsize=(4, 6))
ax[0].plot(data, '.')
ax[0].set_title('Log normal data values')

ax[1].hist(data, 25)
ax[1].set_title('Log normal dist histogram')

plt.show()

###################

n = 10
p = .5

x = range(n + 2)
bindist = stats.binom.pmf(x, n, p)

plt.bar(x, bindist)
plt.title(f'Binomial distribution: n={n}, p={p}\n(coinflip chance of heads)')
plt.show()

###################

x = np.linspace(-4, 4, 1001)
df = 200
t = stats.t.pdf(x, df)

plt.plot(x, t)
plt.xlabel('t-value')
plt.ylabel('P(t|H0')
plt.title(f't({df}) distribution')
plt.show()

####################

num_df = 5
den_df = 100  # Denominator

x = np.linspace(0, 10, 10001)

f_dist = stats.f.pdf(x, num_df, den_df)

plt.plot(f_dist)
plt.title(f'F({num_df}, {den_df}) distribution')
plt.xlabel('F value')
plt.show()