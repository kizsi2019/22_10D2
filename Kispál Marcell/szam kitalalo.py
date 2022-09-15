import random

szam = random.randint(1, 5)
szam2 = int(input("adj meg egy számot! "))
if szam == szam2:
    print("Eltalaltad!")
elif szam2 < szam:
    print("kisebb")
else:
    print("Nagyobb")
print("A gondolt szam: ", szam)
