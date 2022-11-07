sor = 1

oszlop = 1
oszlop2 = 6
oszlop3 = 1
oszlop4 = 1

sex = 1
while sor <= 3:
    while oszlop4 <=oszlop -1:
        print(' ', end='')
        oszlop4 += 1
    print('o ', end='')
    oszlop += 1
    while oszlop3 != oszlop2:
        print(' ', end='')
        oszlop3 += 1
    print('o ', end='')
    oszlop2 -= 2
    print('')
    oszlop4 = 1
    oszlop3 = 1
    sor = sor + 1
sor = sor - 1
print('   o ')

oszlop4 = 2
while sor > 0:
    while oszlop4 <=oszlop -1:
        print(' ', end='')
        oszlop4 += 1
    print('o ', end='')
    oszlop -= 1
    while oszlop3 <= oszlop2:
        print(' ', end='')
        oszlop3 += 1
    print('o ', end='')
    oszlop2 += 2
    print('')
    oszlop4 = 2
    oszlop3 = 1
    sor = sor - 1