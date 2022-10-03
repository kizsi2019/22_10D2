nevek = ['Tonya','Timi','tanga','torony', 'Ottó', 'Sanyi', 'Tamara', 'kiskutyafüle', 'Takarodj']
nevek2 = []

print('T-vel kezdődő szavak:')
for nev in nevek:
    if nev[0] == 'T' or nev[0] == 't':
        print(nev)
nevek.append(nev)

print('Nem t-vel kezdődő szavak:')
for nev2 in nevek:
    if nev2[0] != 't' and nev2[0] != 'T':
        print(nev2)
nevek2.append(nev2)

