import random

osszeg= 5
veletlen_lista=[]

for i in range(5):
    veletlen_szam = random.randint(1,7)
    lista = ['1', '2', '3', '4', '5', '6', '7']
    talalat = False
    index = 0

    talalat = False
    index = 0
    while index <len(lista) and not talalat:
        if lista[index] == '2':
            talalat = True
        index = index + 1
    print("")