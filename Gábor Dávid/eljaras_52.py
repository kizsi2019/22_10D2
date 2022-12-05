def mezot_rajzol(x,y):
    szam1 = int(input("Melyik sorba rajzoljam az x-et? "))
    szam2 = int(input("Melyik oszlopba rajzoljam az x-et? "))
    for sor in range(x):
        for oszlop in range(y):
            if (sor == szam1 - 1) and (oszlop == szam2 -1):
                print('x', end='')
            else:
                print('0', end='')
        print()

mezot_rajzol(3,6)