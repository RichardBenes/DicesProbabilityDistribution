import random as rnd
import matplotlib.pyplot as plt

results = [rnd.randint(1,6) for _ in range(100000)]

plt.hist(results)
plt.show()
