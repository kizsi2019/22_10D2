lista = [0]
szam = int(input("adj meg egy szamot"))

while szam != '':
    szam = input("adj meg egy szamot")
    lista.append(szam)

min = lista[0]
max = lista[0]
for szam in lista:
    if szam < min:
        min = szam
    if szam > max:
        max = szam

print("A legkisseb",min)
print('a legnagyobb' ,max)