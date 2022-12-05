lista = []
min = lista[0]
max = lista[0]
szam = int(input('Adj meg egy számot, ha nem akarsz többet megadni, nyomj ENTER-t!'))
while szam != '':
    lista.append(szam)
for elem in lista:
    if elem < min:
        min = elem
    if elem > max:
        max = elem
print('A megadott számok közül ez volt a legnagyobb: ', max)
print('A megadott számok közül ez volt a legkisebb: ', min)
print('Ezek voltak a megadott számok: ', lista)