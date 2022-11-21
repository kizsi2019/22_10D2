import random

numbalist = []

for i in range(10):
    numba = random.randint(0, 50)
    if numba % 4 == 0:
        numbalist.append(numba)

print(numbalist)