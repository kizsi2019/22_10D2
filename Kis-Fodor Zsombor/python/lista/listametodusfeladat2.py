import random

numbalist = []

for i in range(10):
    numba = random.randint(1, 3)
    numbalist.append(numba)

print(numbalist)

numbertoremove = int(input("give me a number I shall remove (it has to be between 1 and 3)"))

for numbers in numbalist:
    if numbers == numbertoremove:
        numbalist.remove(numbers)

if numbalist[-1] == numbertoremove:
    numbalist.remove(-1)

print(numbalist)