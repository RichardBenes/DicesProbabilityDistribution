import random as rnd
import matplotlib.pyplot as plt
from time import time

start = time()
results = [rnd.randint(1,6) for _ in range(100000)]
stop = time()

plt.hist(results)

stop2 = time()

print(f"Generating results took {stop - start}, rendering {stop2 - stop}.")

plt.show()
