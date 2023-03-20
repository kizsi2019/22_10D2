import random

tarolo = []
for i in range(4):
    lista = []
    for j in range(3):
        lista.append(random.randint(0, 25))
    tarolo.append(lista)

print(tarolo)
