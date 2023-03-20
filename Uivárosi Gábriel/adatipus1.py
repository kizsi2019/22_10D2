import random
tarolo = []
for i in range(4):
    egy_lista = []
    for j in range(3):
        egy_szam = random.randint(0, 25)
        egy_lista.append(egy_szam)
    tarolo.append(egy_lista)
print(tarolo)