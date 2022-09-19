szam = int(input("Adj meg egy páros számot! "))

while szam % 2 == 1:
    szam = int(input("Ez a szám nem páros! "))
else:
    print("A szám páros!")