import matplotlib.pyplot as plt
import numpy as np

c = np.array([1, 10, 4, 3])

prob = 100 * c / np.sum(c)
print(prob)

blue = 40
yellow = 30
orange = 20
total_marbles = blue + yellow + orange

jar = np.hstack((1 * np.ones(blue), 2 * np.ones(yellow), 3 * np.ones(orange)))

number_of_draws = 5000000
color_of_draw = np.zeros(number_of_draws)

for draw in range(number_of_draws):
    random_marble = int(np.random.rand() * len(jar))

    color_of_draw[draw] = jar[random_marble]

propBlue = sum(color_of_draw == 1) / number_of_draws
propYell = sum(color_of_draw == 2) / number_of_draws
propOran = sum(color_of_draw == 3) / number_of_draws

plt.bar([1, 2, 3], [propBlue, propYell, propOran], label='Proportion')
plt.plot([0.5, 1.5], [blue / total_marbles, blue / total_marbles], 'b', linewidth=3, label='Probability')
plt.plot([1.5, 2.5], [yellow / total_marbles, yellow / total_marbles], 'b', linewidth=3)
plt.plot([2.5, 3.5], [orange / total_marbles, orange / total_marbles], 'b', linewidth=3)

plt.xticks([1, 2, 3], labels=('Blue', 'Yellow', 'Orange'))
plt.xlabel('Marble color')
plt.ylabel('Proportion/probability')
plt.legend()
plt.show()
