import string
import random



letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
letter2 = []

index = 0
oszlop = int(input('Hány oszlopos legyen?'))
for szo in letter:
   if index < oszlop:
       letter2.append(szo)
   index += 1
print(letter2)


randomLetter = random.choice(letter2)
szam = random.randint(1, 10)
szam2 = str(szam)
eredmeny = randomLetter+szam2
print(eredmeny)





talalat = 0
tipp = None
while tipp != eredmeny:
    tipp = input("Add meg a sort és az oszlopot")
    if tipp != eredmeny:
        talalat += 1
    if tipp == eredmeny:
        print('ügyes vagy')
        talalat += 1

print('Ennyi próbálkozásból sikerült', talalat)


