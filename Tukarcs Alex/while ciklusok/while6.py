import random

szam = 0

while szam <= 20:
    szam2 = random.randint(1, 12)
    if szam2 % 2 == 1:
        print(szam2)
    szam += 1