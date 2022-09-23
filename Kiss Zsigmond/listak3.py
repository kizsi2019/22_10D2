nevek = []
nev = None
while nev != '':
    nev = input('Adj meg egy kis a nagy A betuvel kezdodo nevet! ')

    if nev != '' and (nev[0] =='a' or nev[0] =='A') :
        nevek.append(nev)
print(nevek)
