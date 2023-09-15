szam = int(input("Adj meg egy páros számot!"))

while szam % 2 == 1:
    szam = int(input("ez a szám páratlan, próbáld újra!"))

if szam % 2 == 0:
    print("ügyes vagy!")