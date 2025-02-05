import random as rnd
import matplotlib.pyplot as plt
import numpy as np

dice_tosses = np.random.randint(1,7, size=(100000,6), dtype=np.byte)

# How much points are they likely to get when there is only one lucky number?

concatenated_1 = np.array([])

for n in range(1,7):
    counts = np.count_nonzero(dice_tosses == n, axis=1)
    concatenated_one_lucky_number = np.concatenate((counts, concatenated_1), axis=0)

print(np.unique(concatenated_1))

plt.hist(concatenated_1, bins=50)
plt.show()

# How much points are they likely to get when there are two lucky numbers?


# And how much points are they likely to get when there are three numbers?


