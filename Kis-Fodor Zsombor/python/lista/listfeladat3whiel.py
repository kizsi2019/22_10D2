import random
numbalist = []
sex = 0
while sex <= 10:
    numba = random.randint(0, 50)
    if numba % 4 == 0:
        numbalist.append(numba)
    sex += 1
print(numbalist)