darab_karakter = int(input("Adj meg egy egy páros számot"))
sor = 1
while sor <= 7:
    oszlop = 1
    while oszlop <= darab_karakter:
        print('O ', end='')
        oszlop = oszlop + 1
    print('')
    darab_karakter = darab_karakter + 1
    sor = sor + 1
