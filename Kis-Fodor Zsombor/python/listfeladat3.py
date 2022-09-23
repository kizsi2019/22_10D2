import random

tenboi = 0
numbalist = []

while tenboi <= 10:
    numba = random.randint(0, 50)
    if numba % 4 == 0:
        numbalist.append(numba)
    tenboi += 1

print(numbalist)