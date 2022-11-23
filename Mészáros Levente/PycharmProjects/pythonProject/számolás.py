import random

szamok = []
páros_számok = []


for i in range(5):
    random_szam = random.randint(1, 10)
    szamok.append(random_szam)

print(szamok)

index = 0

for szam in szamok:
    if szam % 2 == 0:
        index += 1
        páros_számok.append(szam)

print(páros_számok)


print(f'ennyi páros szám van a listában {index}')