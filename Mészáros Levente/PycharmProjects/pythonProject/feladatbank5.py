# Készíts egy függvényt, amely egy adott számlistát vár bemenetként, majd visszaadja az összes páros számot a listában.
#előre megadott számokkal
def szamok():
    szamok = [1, 3, 2, 8, 9, 4, 6]
    paros_szamok = [szam for szam in szamok if szam % 2 == 0]
    return paros_szamok
print(szamok())

#adatbekéréssel
def szamok():
    szamok = []
    while (szam := int(input('adj meg egy számot'))) >= 0:
        szamok.append(szam)
        paros_szamok = [szam for szam in szamok if szam % 2 == 0]
    return paros_szamok
print(szamok())

# véletlen számmal
def szamok():
    import random
    szamok = []
    for i in range(7):
        random_szam = random.randint(1, 10)
        szamok.append(random_szam)
    print(szamok)
    paros_szamok = [random_szam for random_szam in szamok if random_szam % 2 == 0]
    return paros_szamok

print(szamok())