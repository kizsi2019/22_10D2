nevek = []

chance = 0

nev = None
while nev != '' and chance < 3:
    nev = input('Adj meg egy nevet! ')
    chance += 1
    if chance == 3:
        # hozzáfűzi a listahoz
        nevek.append(nev)
print(nevek)
