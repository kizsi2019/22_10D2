szam1 = int(input("Add meg hány sor legyen! "))
szam2 = int(input("Add meg hány oszlop legyen! "))

def mezot_rajzol(x,y):
    for sor in range (x):
        for oszlop in range(y):
            if (sor == szam1 - 1) and (oszlop == szam2 - 1):
                print('x', end='')
            else:
                print('0', end='')
        print()

mezot_rajzol(szam1,szam2)