import random

szamok = []

for i in range(5):
    random_szam = random.randint(1, 10)
    szamok.append(random_szam)

index = 0
for random_szam in szamok:
    if random_szam % 2 == 0:
        index += 1

print(f'ennyi páros szám van a listában {index}')
print(szamok)

