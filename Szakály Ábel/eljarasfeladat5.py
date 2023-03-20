def mezot_rajzol(x,y):

    for sor in range(x):
        for oszlop in range(y):
            if sor == 0 and oszlop == 4:
                print('+ ', end='')
            else:
                print('o ', end='')
        print()


mezot_rajzol(3,6)