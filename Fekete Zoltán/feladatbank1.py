import random


def parosok(lista):

    paros = []
    for szam in lista:
        if szam % 2 == 0:
            paros.append(szam)
    return paros


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
parosak = parosok(lista)
print(parosok)
