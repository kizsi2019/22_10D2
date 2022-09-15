import random

szam = random.randint(1,5)
szam2 = int(input("adj meg egy számot"))
if szam == szam2:
    print("Eltaláltad")
elif szam > szam2:
    print("kisebb")
else:
    print("nagyobb")
print("a gondolt szám: ", szam)