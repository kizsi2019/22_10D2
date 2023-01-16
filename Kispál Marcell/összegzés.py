import random

osszeg = 0
veletlen_lista =[]
for i in range(5):
    veletlen_szam = random.randint(1,10)
    osszeg = osszeg + veletlen_szam
    veletlen_lista.append(veletlen_szam)
print('A lista összege', osszeg)
print(veletlen_lista)