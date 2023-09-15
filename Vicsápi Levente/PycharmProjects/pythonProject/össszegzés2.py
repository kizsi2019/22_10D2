import random

szamok = []


random_szam = random.randint(-5, 5)

szam = 0
while -5 < szam < 5:
    szam = int(input("Adj meg egy számot!"))
    if -5 < szam < 5:
        szamok.append(szam)

print(szamok)

osszeg = 0
for szam in szamok:
    osszeg = osszeg + szam

print(osszeg)


