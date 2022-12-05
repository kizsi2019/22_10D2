szavak = []



szo = None
while szo != '':
    szo = input("Adj meg egy szót!")
    if szo != '':
        szavak.append(szo)


min = szavak[0]
max = szavak[0]

for szo in szavak:
    if szo > max:
        max = szo
    if szo < min:
        min = szo


print(szavak)
print(f'ez a leghosszabb szó {max}')
print(f'ez a legrövidebb szó {min}')