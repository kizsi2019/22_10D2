fakt = 1
szam = int(input('Melyik szám faktoriálisát számolja'))

for i in range(szam):
    fakt = fakt*(i+1)
print(fakt)