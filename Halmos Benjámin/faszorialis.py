fakt = 1
szam = int(input('minek a faktorialisat szamoljam ki?'))

for i in range(szam):
    fakt = fakt * (i+1)

print(fakt)