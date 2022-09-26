szam = int(input("Adj meg egy számot 1 és 10 között"))
while not 1 <= szam <= 10:
    szam = int(input("mondom 1 és 10 között te fasz"))
if szam % 2 == 0:
    print("a szám páros!")
else:
        print("a szám páratlan")
