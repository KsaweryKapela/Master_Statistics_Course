import matplotlib.pyplot as plt
import numpy as np

N = 10000
spike_duration = 10
spike_A = .01
spike_B = .05

spike_tsA = np.zeros(N)
spike_tsB = np.zeros(N)

spike_times_A = np.random.randint(0, N, int(N * spike_A))

for spike_i in range(len(spike_times_A)):
    bnd_pre = int(max(0, spike_times_A[spike_i] - spike_duration / 2))
    bnd_pst = int(min(N, spike_times_A[spike_i] + spike_duration / 2))

    spike_tsA[bnd_pre:bnd_pst] = 1

spike_times_B = np.random.randint(0, N, int(N * spike_B))

for spike_i in range(len(spike_times_B)):
    bnd_pre = int(max(0, spike_times_B[spike_i] - spike_duration / 2))
    bnd_pst = int(min(N, spike_times_B[spike_i] + spike_duration / 2))

    spike_tsB[bnd_pre:bnd_pst] = 1


plt.plot(range(N), spike_tsA, range(N), spike_tsB)
plt.ylim([0, 1.2])
plt.xlim([2000, 2500])
plt.show()

probA = sum(spike_tsA == 1) / N
probB = np.mean(spike_tsB)

probAB = np.mean(spike_tsA + spike_tsB == 2)

A_given_B = probAB / probB

B_given_A = probAB / probA

print('P(A)   = %g' % probA)
print('P(A|B) = %g' % A_given_B)
print('P(B)   = %g' % probB)
print('P(B|A) = %g' % B_given_A)
