szam = int(input("Adj meg egy számot!"))
szam2 = int(input("Adj meg egy másik számot!"))
szam3 = int(input("Adj meg egy harmadik számot!"))

if szam < szam2 and szam < szam3:
    print('Az első szám a legkisebb' ,szam)

if szam2 < szam and szam2 < szam3:
    print('A második szám a legkisebb' ,szam2)

if szam3 < szam and szam3 < szam2:
    print('A harmadik szám a legkisebb' ,szam3)




