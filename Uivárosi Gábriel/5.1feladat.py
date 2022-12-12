
def mezot_rajzol():
    T = True
    while T == True:
        S = int(input("Agyon meg sor "))
        O = int(input(" Agyon meg oszlopot "))
        if S < 0 or O < 0:
            T = False
        for sor in range(5):
            for oszlop in range(13):
                if S == sor and O == oszlop:
                    print('+ ', end='')
                else:
                    print('O ', end='')
            print()

mezot_rajzol()