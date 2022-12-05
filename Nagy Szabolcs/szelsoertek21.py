szavak = []
szo = None


while szo != '':
    szo = input("Adj meg egy szót!")
    if szo != '':
        szavak.append(szo)
print(szavak)
min = szavak[0]
max = szavak[0]

for szo in szavak:
    if szo > max:
        max = szo
    if szo < min:
        min = szo

print("A leghosszabb szó:", max)
print("A legrövidebb szó:", min)