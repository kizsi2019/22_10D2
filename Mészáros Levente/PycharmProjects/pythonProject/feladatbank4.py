#Készíts egy függvényt, amely egy adott számlistát vár bemenetként, majd visszaadja a listában található számok átlagát.
# előre megadott adatok


def szamok(*args):
    darab = 0
    osszeg = 0
    for szam in args:
        osszeg = osszeg + szam
        darab += 1
    atlag = osszeg / darab
    return atlag

print(szamok(5, 1))

# adatbekéréssel
def szamok(*args):
    darab = 0
    osszeg = 0
    while(szam := int(input('adj meg egy számot'))) > 0:
        osszeg = osszeg + szam
        darab += 1
    atlag = osszeg / darab
    return atlag

print(szamok())

# véletlen számmal
def szamok(*args):
    import random
    darab = 0
    osszeg = 0
    for i in range(5):
        random_szam = random.randint(1, 10)
        osszeg = osszeg + random_szam
        darab += 1
    atlag = osszeg / darab
    return atlag

print(szamok())