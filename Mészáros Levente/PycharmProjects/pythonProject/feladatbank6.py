# Készíts egy függvényt, amely egy adott számlistát vár bemenetként, majd visszaadja a listában található legkisebb és legnagyobb szám közötti különbséget.
# előre megadott számokkal
def szamok(*args):
    return min(args) - max(args)
print(szamok(1,6,7,4,5,2,3))

# adatbekéréssel
def szamok():
    szamok = []
    while (szam := int(input('adj meg egy számot'))) > 0:
        szamok.append(szam)
    return min(szamok) - max(szamok)
print(szamok())

# véletlen számmal
def szamok():
    import random
    szamok = []
    for i in range(7):
        random_szam = random.randint(1, 10)
        szamok.append(random_szam)
    print(szamok)
    return min(szamok) - max(szamok)
print(szamok())