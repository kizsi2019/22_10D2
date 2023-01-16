def mezot_rajzol(x,y):
    for sor in range (x):
        for oszlop in range(y):
            if sor == 0 and oszlop == 4:
                print('x', end='')
            else:
                print('0', end='')
        print()

mezot_rajzol(4,5)