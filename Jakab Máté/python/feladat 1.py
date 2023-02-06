import random

def generate_lists():
    tarolo = []
    for i in range(4):
        lista = []
        for j in range(3):
            szam = random.randint(0, 25)
            lista.append(szam)
        tarolo.append(lista)
    return tarolo

tarolo = generate_lists()
print(tarolo)