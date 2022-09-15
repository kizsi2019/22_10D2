import random

szam = random.randint(-5, 5)

print(f'A gondolt szám {szam}')

if szam % 2 == 0:
    print("A szám páros")
else:
    print("A szám páratlan")

