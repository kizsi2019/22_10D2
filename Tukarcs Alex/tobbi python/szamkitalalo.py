import random

szam = random.randint(1,5)
szam2 = int(input("Adj meg egy számot"))
if szam == szam2:
    print("Eltaláltam")
elif szam > szam2:
    print("Kisebb")
else:
    print("Nagyobb")
print("A gondolt szam", szam)