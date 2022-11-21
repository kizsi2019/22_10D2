lista = []
min = [0]
max = [0]

szam = int(input('Adj meg egy számot!'))
while szam != "":
    szam = int(input('Adj meg egy számot!'))
lista.append(szam)
for szam in lista:
    if szam < min:
        min = szam
    if szam > max:
        max = szam
print('A legkisebb szám a listában: ', min)
print('A legnagyobb szám a listában: ', max)

