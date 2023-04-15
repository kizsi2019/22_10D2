print('1. feladat')
szam = int(input('add meg a dobésok számát'))

print('\n2.feladat')
import random
dobasok = []
for dobas in range(1, szam + 1):
    random_szam = random.randint(1, 6)
    dobasok.append(random_szam)
print(f'A dobások: {dobasok}')

print('\n3.feladat')
osszeg = 0
darab = 0
for dobas in dobasok:
    osszeg = osszeg + dobas
    darab += 1

atlag = osszeg / darab

print(f'A játékos átlagosan {atlag:.2f} mezőt, összesen {osszeg:.0f} mezőt haladt előre.')


print('\n4.feladat')
index = 0
talalat = None
darab = 0
while index < len(dobasok):
    if dobasok[index] == 6:
        talalat = True
        darab += 1
    index += 1

if talalat:
    print(f'A játékos {darab} alkalommal dobott hatost')

if not talalat:
    print('A játékos sajnos egy alkalommal sem dobott hatost')

print('\n5.feladat')
index = 0
talalat = None
darab = 0
while index < len(dobasok):
    if dobasok[index] % 2 == 0:
        talalat = True
        darab += 1
    index += 1

print(f'A játékos {darab} alkalommal dobott páros számot.')

print('\n6.feladat')
darab = 0
for index in range(szam - 1):
    if 0 < dobasok[index] > dobasok[index + 1]:
        darab += 1

print(f'A játékos {darab} alkalommal dobott kevesebbet, mint előző körben.')