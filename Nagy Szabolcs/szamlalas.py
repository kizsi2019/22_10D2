import random

szamok = []

for i in range(5):
    szam = random.randint(1, 10)
    szamok.append(szam)

index = 0

for szam in szamok:
    if szam % 2 == 0:
        index = index + 1

print('A listában lévő páros számok mennyisége: ', index)
print("A lista elemei:", szamok)
