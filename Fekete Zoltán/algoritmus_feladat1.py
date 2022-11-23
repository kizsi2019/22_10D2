import random
osszeg = 0
veletlen_lista = []

for i in range(5):
    szam = random.randint(1, 10)
    osszeg = osszeg + szam
    veletlen_lista.append(szam)
    print('A lista: ', veletlen_lista)
    print('A lista összege: ', osszeg)
