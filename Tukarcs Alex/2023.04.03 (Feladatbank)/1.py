def kiválogat_párosak(list):
    párosak = []
    for szám in list:
        if szám % 2 == 0:
            párosak.append(szám)
            print(szám, end=' ')
    return párosak

számok = [1, 2, 3, 4, 5, 6, 7, 8, 9]
kiválogat_párosak(számok)
