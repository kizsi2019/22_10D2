while True:
    szam = int(input('Adj meg egy a [-100.000;100.000] tartományba eső egész számot!'))
    abszolut_ertek = abs(szam)
    oszthato_ottel = None
    sorsz = 0
    if szam < -100000 or szam > 100000:
        break
    if szam % 2 == 1 and szam % 3 == 0:
        print('\n2.feladat')
        print('A szám páratlan és osztható hárommal')

    if szam % 2 == 1 and not szam % 3 == 0:
        print('\n2.feladat')
        print('A szám páratlan és nem osztható hárommal')

    if szam % 2 == 0 and szam % 3 == 0:
        print('\n2.feladat')
        print('A szám páros és osztható hárommal')

    if szam % 2 == 0 and not szam % 3 == 0:
        print('\n2.feladat')
        print('A szám páros és nem osztható hárommal')

    print('\n3.feladat')
    print(f'A szám abszolút értéke: {abszolut_ertek}')

    print('\n4.feladat')
    if szam % 5 == 0:
        print('A szám osztható öttel')
        oszthato_ottel = True

    else:
        print('A szám nem osztható öttel')
        oszthato_ottel = False


    if not oszthato_ottel:
        szam2 = round(szam, -1)

        if szam2 < szam:
            print(f'A szám abszolút értékéhez legközelebb eső, nála nagyobb öttel osztható szám a(z) {szam2 + 5}.')

        elif szam2 > szam:
            print(f'A szám abszolút értékéhez legközelebb eső, nála nagyobb öttel osztható szám a(z) {szam2}.')

    print('\n5.feladat')

