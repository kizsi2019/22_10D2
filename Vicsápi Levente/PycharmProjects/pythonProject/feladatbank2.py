# Készíts egy függvényt, amely egy adott számlistát vár bemenetként, majd visszaadja a listában található legnagyobb számot.
# számmal megadva
def szamok(x, *args):
    max = x
    for szam in args:
        if szam > max:
            max = szam
    return max

print(szamok(1,3,6,9,7,4,2))

# adatbekérés
def pozitiv():

    szamok = []


    szam = 1
    while szam > 0:
        szam = int(input("adj meg egy számot"))
        if szam >= 0:
            szamok.append(szam)
    print(szamok)
    return max(szamok)

print(pozitiv())


def veletlen(szam):
    szamok = []
    import random
    for i in range(5):
        random_szam = random.randint(1, 10)
        szamok.append(random_szam)
    for random_szam in szamok:
        min = szamok[0]
        max = szamok[0]
        if random_szam < min:
            min = random_szam
        if random_szam > max:
            max = random_szam
    print(szamok)
    return max

print(veletlen(szam=''))