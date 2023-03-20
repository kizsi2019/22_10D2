szam = int(input("adj meg egy számot!"))
szam2 = int(input("adj meg egy számot!"))

if szam > szam2:
    print("nagyobb érték", szam)

if szam2 > szam:
    print("nagyobb érték", szam2)

if szam2 == szam:
    print("a két szám egyenlő")