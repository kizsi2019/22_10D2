# Készíts egy függvényt, amely egy adott számlistát vár bemenetként, majd visszaadja a lista elemeit megfordítva.
# előre megadott számokkal

def szamok():
    szamok = [1, 3, 4, 8, 9, 7, 5]
    szamok.reverse()
    return szamok
print(szamok())

# adatbekéréssel
def szamok():
    szamok = []
    while (szam := int(input('adj meg egy számot'))) > 0:
        szamok.append(szam)
    szamok.reverse()
    return szamok

print(szamok())

# véletlen számokkal
def szamok():
    import random
    szamok = []
    for i in range(7):
        random_szam = random.randint(1, 10)
        szamok.append(random_szam)
    szamok.reverse()
    return szamok
print(szamok())