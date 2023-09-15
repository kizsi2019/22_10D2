def harommal_oszthato(x, *szamok):

    darab = 1
    for szam in szamok:
        if szam % 2 == 1:
            darab += 1

    return darab

print(harommal_oszthato(1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13, 16, 69, 99))