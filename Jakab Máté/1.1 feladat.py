nevek= []

nev = None
szam = 1
while nev!= '' and szam <= 3:
    nev = input('Adj meg egy nevet!')
    if nev != '':

        nevek.append(nev)
        szam = szam + 1

print("A programm vége")
print(nevek)
