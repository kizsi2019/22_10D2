import random
osszeg = 0
veletlen_lista = []

for i in range(5):
    szam = random.randint(1, 10)
    if szam % 2 == 0:
        osszeg = osszeg + szam
    veletlen_lista.append(szam)
    print('A lista összege: ', osszeg)
    print(veletlen_lista)
