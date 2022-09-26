sor = 1
while sor <= 5:
    oszlop = 1
    while oszlop <= 7:
        if oszlop == 1 and sor == 1:
            print('O ', end='')
        else:
            print(' ', end='')
        if oszlop > 7:
            print()
        if oszlop == 7 and sor == 1:
            print('O ', end='')
        else:
            print(' ', end='')
        if oszlop == 1 and sor == 2:
            print('O ', end='')
        else:
            print(' ', end='')
        if oszlop == 6 and sor == 2:
            print('O ', end='')
        else:
            print(' ', end='')
        if oszlop == 1 and sor == 3:
            print('O ', end='')
        else:
            print('', end='')
        if oszlop == 5 and sor == 3:
            print('O ', end='')
        else:
            print('', end='')
        if oszlop == 4 and sor == 4:
            print(' O', end='')
        else:
            print('', end='')
        if oszlop == 1 and sor == 4:
            print('  0', end='')
        else:
            print('', end='')

        if oszlop == 2 and sor == 5:
            print('0', end='')
        else:
            print('', end='')

        if oszlop == 4 and sor == 5:
            print(' 0', end='')
        else:
            print('', end='')










        oszlop = oszlop + 1
    print('')
    sor = sor + 1
