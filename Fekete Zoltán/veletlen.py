import random

szam = random.randint(1, 3)
szam2 = int(input("Adj meg egy számot!"))

if szam == szam2:
    print("Eltaláltad!")
else:
    print("Nem találtad el!")