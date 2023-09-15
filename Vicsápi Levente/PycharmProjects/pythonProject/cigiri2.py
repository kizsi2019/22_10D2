def osszegzo(x, *szamok):

    osszeg = x
    for x in szamok:
        if szam % 2 == 0:
        osszeg = osszeg + x




print(osszegzo(3,5))