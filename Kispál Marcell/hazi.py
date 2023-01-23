szavak = []

szo = None
while szo != '':
    szo = input("adj meg egy betűt")
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
print(f'leghosszabb {max}')
print(f'legrövidebb {min}')
