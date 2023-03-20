import random
lista = []
darab = 0
for i in range(50):
    szam = random.randint(1,100)
    lista.append(szam)
for szam2 in lista:
    if szam2 % 2 == 0:
        darab = darab + 1
print(lista)
print('Ennyi szam oszthato 2vel:', darab)