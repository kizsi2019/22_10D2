import random

jeez = 0
szamok = []

while jeez <= 10:
    szam = random.randint(0, 50)
    if szam % 4 == 0:
        szamok.append(szam)
    jeez += 1

print(szamok)