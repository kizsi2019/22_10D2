def paros_e(x, *szamok):
    for szam in szamok:
        if szam % 2 == 0:
            return True
        elif szam % 3 == 0:
            return False

print(paros_e(1,5,3,9))