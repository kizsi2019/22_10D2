szam = int(input("Adj meg egy számot!"))

darab_karakter = 1
sor = 1
while sor <= szam / 2:
    oszlop = 1
    while oszlop <= darab_karakter:
        print('O ', end='')
        oszlop = oszlop + 1
    print('')
    darab_karakter = darab_karakter + 1
    sor = sor + 1

sor = sor + 1
darab_karakter = darab_karakter - 1

while sor > 0:
    oszlop = 1 
    while oszlop <= darab_karakter:
        print('O ', end='')
        oszlop = oszlop + 1
    print('')
    darab_karakter = darab_karakter - 1
    sor = sor - 1
