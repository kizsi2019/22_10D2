import random
import string
lista = ['A', 'B', 'C']
lista2 = []

index = 0
oszlop = int(input('Hány oszlop legyen a pályán?'))
for szo in lista:
    if index < oszlop:
        lista2.append(szo)
    index = index + 1

hajo = random.choice(lista2)
szam = random.randint(1,3)
szam2 = str(szam)
xyz = hajo + szam2

talalat = 0
tipp = None
while tipp != xyz:
    tipp = input('Add meg a sor és oszlop amire tippelsz!')
    if tipp != xyz:
        print('Nem találtad el, próbáld újra!')
        talalat += 1
    if tipp == xyz:
        print('Eltaláltad a célt!')
        talalat = talalat + 1
print('Ennyi próbálkozásból találtad el: ', talalat)