import random

szam = 1
db= 0

while szam <= 20:
    veletlen_szam = random.randint(1, 12)
    if veletlen_szam % 3 == 0:
        print(veletlen_szam)
        db= db +1
    szam += 1
print("Ennyi 3-mal osztható számot találtam: ", db)
