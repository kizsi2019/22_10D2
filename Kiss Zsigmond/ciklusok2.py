darab_karakter = 1
sor = 1
while sor <= 5:
    oszlop = 1
    while oszlop <= darab_karakter:
        if oszlop == darab_karakter:
            print('O ', end='')
        else:
            print(' ', end='')
        oszlop = oszlop + 1
    print('')
    darab_karakter = darab_karakter + 1
    sor = sor + 1