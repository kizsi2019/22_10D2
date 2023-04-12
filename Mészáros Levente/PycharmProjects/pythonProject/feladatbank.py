#  Készíts egy függvényt, amely egy adott számlistát vár bemenetként, majd visszaadja az összes páros számot a listában.
# számokkal a listában
def szamok():
    paros_szamok = [1, 5, 3, 7, 8, 2, 4, 0]
    print('páros számok a listában:')
    for szam in paros_szamok:
        if szam % 2 == 0:
            print(szam)
    return paros_szamok
print(szamok())

# adatbekéréssel a listában
def szamok2():
    paros_szamok = []
    while (szam := int(input('adj meg egy számot!'))) > 0:
        paros_szamok.append(szam)
    print('páros számok a listában:')
    for szam in paros_szamok:
        if szam % 2 == 0:
            print(szam)
    return paros_szamok
print(szamok2())




# véletlenszámokkal a listában
def szamok3():
    import random
    paros_szamok = []
    print('páros számok a listában:')
    for i in range(5):
        random_szam = random.randint(1, 10)
        paros_szamok.append(random_szam)
        if random_szam % 2 == 0:
            print(random_szam)
    return paros_szamok

print(szamok3())