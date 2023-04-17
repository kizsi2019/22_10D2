Diák = input("Add meg a vizsgázó nevét:")
Pontszám = int(input("Add meg a vizsgázó pontszánát:"))

if Pontszám < 48:
    print(Diák,"vizsgája sikertelen.")

if Pontszám > 48:
    print(Diák,"vizsgája sikeres.")

if Pontszám == 48:
    print(Diák,"vizsgája sikeres.")