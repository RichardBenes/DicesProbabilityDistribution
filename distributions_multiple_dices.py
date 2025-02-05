import matplotlib.pyplot as plt
from matplotlib.ticker import EngFormatter
import numpy as np
from itertools import combinations

tosses_shape = (100000,6)
allowed_values = [1,2,3,4,5,6]
n_of_dices = 6

dice_tosses = np.random.randint(1,7, size=tosses_shape, dtype=np.byte)

fig, ax = plt.subplots(1, n_of_dices, sharey=True)
plt.gca().yaxis.set_major_formatter(EngFormatter(places=0))

for n_of_values in range(1,n_of_dices+1):

    points_scored = np.array([], dtype=np.uint32)

    created_combinations = combinations(allowed_values, n_of_values)

    print(f"There are {len(list(combinations(allowed_values, n_of_values)))}"
          + " combinations when {n_of_values} values are drawn from {allowed_values}.")

    for combination in created_combinations:
        hits = np.zeros(tosses_shape) == 1
        for comb_idx in range(n_of_values):
            hits = hits | (dice_tosses == combination[comb_idx])

        counts = np.count_nonzero(hits, axis=1)
        points_scored = np.concatenate((counts, points_scored), axis=0)

    counts = np.bincount(points_scored)
    x_values = np.unique(points_scored)

    print(len(points_scored))

    ax[n_of_values-1].bar(x_values, counts, align="center")


plt.show()
