lista = []


while (szam := int(input('adj meg egy számot'))):
        lista.append(szam2)

min = lista[0]
max = lista[0]
for szam2 in lista:
    if szam2 < min:
        min = szam2
    if szam > max:
        max = szam2

print(f'a legnagyobb szám a listában {max}')
print(f'a legkisebb szám a listában {min}')