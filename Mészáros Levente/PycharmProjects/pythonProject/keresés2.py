import random

szamok = []

for i in range(5):
    random_szam = random.randint(1, 7)
    szamok.append(random_szam)


szam = int(input("Adj meg egy számot"))

talalat = False
index = 0

while index < len(szamok) and not talalat:
    if szamok[index] == szam:
        talalat = True
    index += 1


if talalat:
    print(f'van ilyen szám a listában: {szam}')

if not talalat:
    print(f'ilyen szám nincs a listában: {szam}')



