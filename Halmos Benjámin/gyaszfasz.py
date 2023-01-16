lista = []
mini = list[0]
maxi = list[0]

szam = int(input("adjon meg egy szamot"))

while szam != '':
    szam = int(input("adjon meg egy szamot"))
    lista.append(szam)

for elem in lista:
    if elem < mini:
        min = szam
    if elem > maxi:
        max = szam

print(lista)
print("legkissebb fasz méret", mini, "cm")
print("legnagyobb fasz méret", maxi, "cm")