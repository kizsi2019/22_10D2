lista = [1, 4, 5, 7, 9, 12, 15]

darab = 0
for szam in lista:
    if szam % 3 == 0:
        darab = darab + 1
print("ennyi szám osztható hárommal:", darab)