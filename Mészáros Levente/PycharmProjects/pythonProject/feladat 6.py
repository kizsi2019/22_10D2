import random

szam = random.randint(1, 12)

ism = 0
while ism < 20:
    szam = random.randint(1, 12)
    if szam % 3 == 0:
        print(szam)
    ism += 1
