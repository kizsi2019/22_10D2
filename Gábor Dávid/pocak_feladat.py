beker = int(input("Adj meg egy páros számot! "))
darab_karakter = 1
sor = 1

while sor <= beker:
    oszlop = 1
    while oszlop <= darab_karakter:
        print('0 ', end='')
        oszlop = oszlop + 1
    print('')
    darab_karakter = darab_karakter + 1
    sor = sor + 1
while sor <= beker:
    oszlop = 1
    while oszlop <= darab_karakter:
        print('0 ', end='')
        oszlop = oszlop - 1
    print('')
    darab_karakter = darab_karakter -1
    sor = sor - 1