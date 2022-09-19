import random




szam = random.randint(1, 5)
szam2 = int(input("Adj meg egy számot"))

while szam2 < szam:
    szam2 = int(input("A szám kissebb "))
while szam2 > szam:
    szam2 = int(input("A szám nagyobb"))

if szam2 == szam:
    print("Talált")


