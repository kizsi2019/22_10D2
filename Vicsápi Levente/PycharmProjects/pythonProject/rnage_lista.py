import random

szamok = []


for i in range(10):
    szam = random.randint(1, 40)
    if szam % 2 == 0:
        szamok.append(szam)
print(szamok)



