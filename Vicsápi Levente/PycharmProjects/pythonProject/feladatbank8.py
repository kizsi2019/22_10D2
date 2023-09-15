# Készíts egy függvényt, amely egy adott számlistát vár bemenetként, majd visszaadja a listában található számok átlagát, és azok közül azoknak az indexeit, amelyek nagyobbak, mint az átlag.
# előre megadott számokkal
def szamok():
    args = [5, 4, 3, 1, 4, 2, 5]
    index = 0
    osszeg = 0
    darab = 0
    for szam in args:
        osszeg = osszeg + szam
        darab += 1
        index += 1
    atlag = round(osszeg / darab)
    print(index)
    return atlag
print(szamok())