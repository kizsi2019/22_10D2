def osszegzo(szamok):
    osszesen = 0
    for szam in szamok:
        osszesen = osszesen + szam
    print('a listában lévő számok öszzege ', osszesen)

szamok = [3, 5, 19, 11, 17, 1]
osszegzo(szamok)