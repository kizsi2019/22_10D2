import random



szamok = []

for i in range(5):
    random_szam =random.randint(1, 7)
    szamok.append(random_szam)

print(szamok)

szam = int(input("Adj meg egy számot"))

talalat = False
index = 0
while index < len(szamok) and not talalat:
    if szamok[index] == szam:
        talalat = True
    index += 1

if talalat:
    print("van ilyen szám a listában")

if not talalat:
    print("ilyen szám nincs a listában")