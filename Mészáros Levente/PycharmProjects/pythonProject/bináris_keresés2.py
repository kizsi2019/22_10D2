import random

talalat = False

szamok = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


szam = int(input("adj meg egy számot!"))

while not talalat:
    random_szam = random.choice(szamok)
    print(random_szam)
    if random_szam < szam:
        szamok.remove(random_szam)
    if random_szam == szam:
        talalat = True
    if talalat:
        break







print(szamok)