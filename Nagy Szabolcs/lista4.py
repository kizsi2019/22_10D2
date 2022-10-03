import random

számok = []

for i in range(10):
    szám = random.randint(0, 50)
    if szám % 4 == 0:
        számok.append(szám)

print(számok)