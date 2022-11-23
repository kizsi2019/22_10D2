nevek = []
szam = 1
nev = None
while nev != '' and szam <= 3:
    nev = input('Adj meg egy nevet! ')
    if nev != '' and nev[0] == 'a':
        nevek.append(nev)
    szam = szam + 1
print("Csak a betűvel kezdődő nevet tárolok!")
print(nevek)