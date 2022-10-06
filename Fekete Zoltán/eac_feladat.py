szam = int(input("Adj meg egy páros számot!"))
darab_karakter = 1
sor = szam/2
while sor <= szam:
    oszlop = 1
    while oszlop <= darab_karakter:
        print('0 ', end='')
        oszlop +=1
    print('')
    darab_karakter += 1
    sor += 1
    darab_karakter -= 1
    sor += 1
    oszlop = darab_karakter / 2
    while oszlop >= darab_karakter:
        print('0 ', end='')
        oszlop -= 1
    print('')
    darab_karakter += 1
    sor -= 1