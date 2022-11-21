import random

osszeg = 0
veletlen_lista = []


for i in range(5):
    veletlen_szam = random.randint(1,10)
    if veletlen_szam %2== 0:
        osszeg = osszeg + veletlen_szam
    veletlen_lista.append(veletlen_szam)

print(veletlen_lista)
print('A lista összege', osszeg)
