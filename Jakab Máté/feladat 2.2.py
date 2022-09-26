nevek = []
nev = None
while nev != '':
    nev = input('Adj meg egy nagy a betuval kezdodo nevet!')

    if nev != '' and (nev[0] =='a' or nev[0] =='A'):
        nevek.append(nev)
        print('helyes')
    else:
        print('nem jo szo')
    print(nevek)