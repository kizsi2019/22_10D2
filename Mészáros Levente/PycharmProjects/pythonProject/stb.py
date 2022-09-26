szam = int(input("adj meg egy számot"))

darab_karakter = 1
sor = 1
while sor <= szam:
    oszlop = 1
    while oszlop <= darab_karakter:
        print('0 ', end='')
        oszlop += 1
    print('')
    darab_karakter = darab_karakter + 1
    sor = sor + 1
darab_karakter = szam
sor = 1
while sor <= szam:
    oszlop = 1
    while oszlop <= darab_karakter:
        print('0 ', end='')
        oszlop += 1
    print('')
    darab_karakter = darab_karakter - 1
    sor = sor + 1




