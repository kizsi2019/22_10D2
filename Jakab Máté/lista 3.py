import random
szam_lista = []
szam = 1
while szam <=10:
    veletlen_szam = random.randint(0, 50)
    print(veletlen_szam)
    if veletlen_szam % 4 == 0:
        szam_lista.append(veletlen_szam)
    szam = szam + 1
print(szam_lista)