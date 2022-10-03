nevek = []
szam = 1
nev = None
while nev != '' and szam <= 3:
    nev = input('Adj meg egy nevet! ')
    if nev != '':
        nevek.append(nev)
    szam = szam + 1
print("Csak 3 nevet tárolok!")
print(nevek)