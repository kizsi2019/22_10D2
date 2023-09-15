import random


szamok = []

for i in range(5):
    szam = random.randint(1, 7)
    szamok.append(szam)
print(szamok)


szam2 = int(input("Adj meg egy számot!"))

talalat = False
index = 0

while index < len(szamok) and not talalat:
    if szamok[index] == szam2:
        talalat = True
    index = index + 1

if talalat:
    print('Van a listában ilyen szám.')
else:
    print('Nincs ilyen szám a listában.')