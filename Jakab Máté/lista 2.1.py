nevek = []
nev = None
while nev != '':
    nev = input('Adj meg egy kis a betuval kezdodo nevet!')

    if nev != '' and nev[0] =='a':
        nevek.append(nev)
    print(nevek)