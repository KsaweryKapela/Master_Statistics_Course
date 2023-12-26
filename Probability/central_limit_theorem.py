import matplotlib.pyplot as plt
import numpy as np

N = 1000000
data = np.random.randn(N) ** 2
# data = np.sin(np.linspace(0,10*np.pi,N))

plt.plot(data, '.')
plt.show()

plt.hist(data, 40)
plt.show()

sample_size = 30
number_of_exps = 500
sample_means = np.zeros(number_of_exps)

for expi in range(number_of_exps):
    sample_idx = np.random.randint(0, N, sample_size)
    sample_means[expi] = np.mean(data[sample_idx])

plt.hist(sample_means, 30)
plt.xlabel('Mean estimate')
plt.ylabel('Count')
plt.show()

###

x = np.linspace(0, 6 * np.pi, 10001)
s = np.sin(x)
u = 2 * np.random.rand(len(x)) - 1

fig, ax = plt.subplots(2, 3, figsize=(10, 6))
ax[0, 0].plot(x, s, 'b')
ax[0, 0].set_title('Signal')

y, xx = np.histogram(s, 200)
ax[1, 0].plot(y, 'b')
ax[1, 0].set_title('Distribution')

ax[0, 1].plot(x, u, 'm')
ax[0, 1].set_title('Signal')

y, xx = np.histogram(u, 200)
ax[1, 1].plot(y, 'm')
ax[1, 1].set_title('Distribution')

ax[0, 2].plot(x, s + u, 'k')
ax[0, 2].set_title('Combined signal')

y, xx = np.histogram(s + u, 200)
ax[1, 2].plot(y, 'k')
ax[1, 2].set_title('Combined distribution')

plt.show()
