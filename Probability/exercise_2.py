import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

np.random.seed(19680801)

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)
ax.plot(x)
ax.set_ylabel("mu + sigma * np.random.randn(x)", color="blue", fontsize=10)
ax.set_xlabel("x", color="blue", fontsize=14)
plt.show()


fig, ax2 = plt.subplots()
n, bins, patches = ax2.hist(x, bins=50, facecolor='g', alpha=0.15)
axc = ax2.twinx()
axc.hist(x, 50, cumulative=True, facecolor='y', alpha=0.15)
ax2.set_xlabel('Smarts')
ax2.set_ylabel('Probability Density', color='g')
axc.set_ylabel('Probability Cummulative', color='y')
ax2.set_title('Histogram of IQ')
ax2.text(60, .025, r'$\mu=100,\ \sigma=15$')
ax2.set_xlim(40, 160)
ax2.grid(True)
plt.show()

fig, ax = plt.subplots()
pdf = n / sum(n)
ax.plot(bins[1:], pdf, color="red", marker='.')
ax.set_xlabel("smarts", fontsize=14)
ax.set_ylabel("pdf", color="red", fontsize=14)
ax2 = ax.twinx()
cdf = np.cumsum(pdf)
plt.plot(bins[1:], cdf, color="blue", marker='+')
ax2.set_ylabel("cdf", color="blue", fontsize=14)
plt.show()