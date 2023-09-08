szam = int(input("Adj meg egy számot! "))
szam2 = int(input("Adj meg egy másik számot! "))

if szam > szam2:
    print("A nagyobb érték: ",szam)
elif szam2 == szam:
    print("A két szám egyenlő!")
else:
    print("A nagyobb érték: ",szam2)