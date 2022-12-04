S = int(input("Agyon meg sor 0-2"))
O = int(input(" Agyon meg oszlopot 0-5"))
def mezot_rajzol():

    
    for sor in range(3):
        for oszlop in range(6):
            if S == sor and O == oszlop:
                print('+ ', end='')
            else:
                print('O ', end='')
        print()

mezot_rajzol()