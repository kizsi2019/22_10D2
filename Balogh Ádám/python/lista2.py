#gyumolcsok = []

#gyumolcs = None
#while gyumolcs != '':
    #gyumolcs = input('Adj meg egy gyümölcsöt! ')
    #if gyumolcs != '':
        #gyumolcsok.append(gyumolcs)

#print(gyumolcsok)

nevek = []

nev = None
szam = 1
while nev!= '' and szam <= 3:
    nev = input('Adj meg egy nevet!')
    if nev != '':

        nevek.append(nev)
        szam = szam + 1

print("A program vége")
print(nevek)


