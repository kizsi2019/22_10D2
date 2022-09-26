nevek = []
szam = 3
nev = None
while nev != '' and szam <=3:
    nev = input('Adj meg egy nevet ')
    if nev != '':
        nevek.append(nev)
    szam = szam + 1
print("csak 3 nevet tárolok")
print(nevek)