import math

a = float(input("1. oldal: "))
b = float(input("2. oldal: "))
c = float(input("3. oldal: "))



if (math.pow(a, 2) + math.pow(b,2) == round(math.pow(c, 2))):
    print("Derékszögű háromszög.")
else:
    print("Nem derékszögű háromszög.")