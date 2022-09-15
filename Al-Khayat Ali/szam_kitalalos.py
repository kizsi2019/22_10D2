import random

szam = random.randint(1,5)
szam2 = int(input("adj meg egy szamot!"))
if szam == szam2:
    print("eltalaltad")
elif szam > szam2:
    print("kisebb")
else:
    print("nagyobb")
print("a gondolt szam: ", szam)
