import random

szam = random.randint(1,3)
szam2= int(input("adj meg egy számot!"))

if szam2 == szam:
    print("talált")
else:
    print("rossz")