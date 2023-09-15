def osszegzo(x, *szamok):

    osszeg = 1
    for szam in szamok:
        osszeg = osszeg + szam

    return osszeg

print(osszegzo(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
