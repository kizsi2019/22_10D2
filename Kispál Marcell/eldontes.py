import random
coord = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3' ]
hely = random.choice(coord)
talalat = False
index = 0
tipp = input("melyik mezőn vam a jajó (A-C : 1-3)? ")
while index < len(coord) and not talalat:
    if tipp == hely:
        talalat = True
    else:
        tipp = input("Melyik mezőn van a hajó (A-C : 1-3)? ")
        index = index + 1

print('Eltaláltad, a próbálkozásaid száma: ', index)