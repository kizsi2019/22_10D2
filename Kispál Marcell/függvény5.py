lista = []
szam = int(input("Adj meg egy számot!"))
while szam > 0:
    lista.append(szam)
    szam = int(input("Adj megz egy számot!"))
def min(lista):
    min = lista[0]
    for elem in lista:
        if elem < min:
            min = elem
    return min
print("A lista legkisebb eleme: "+ min(lista))
