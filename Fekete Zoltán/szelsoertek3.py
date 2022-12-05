szavak = []

szo = input('Adj meg egy szót!')
for szo in szavak:
    print(szavak)
while szo != '':
    szavak.append(szo)
    szo = input('Adj meg egy szót! Ha nem akarsz többet megadni, nyomj ENTER-t!')
min = szavak[0]
max = szavak[0]
for szo in szavak:
    if len(szo) < len(min):
        min = szo
    if len(szo) > len(max):
        max = szo
print(szavak)
print("A legrövidebb szó ez volt: ", min)
print("A leghosszabb szó ez volt: ", max)
