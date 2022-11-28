fakt = 1
szam = int(input('melyik szám faktoriálisát számoljam'))

for i in range(szam):
    fakt = fakt * (i+1)
print(fakt)