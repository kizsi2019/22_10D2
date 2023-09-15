import random
szamok = []
szamok2 = []
darab = 0

for i in range(10):
    szam = random.randint(1, 3)
    szamok.append(szam)
print(szamok)
szam2 = int(input('Adj meg egy számot'))


for i in szamok:
    if szam2 == szamok[i]:
        szamok.remove(szamok[i])
print(szamok)







