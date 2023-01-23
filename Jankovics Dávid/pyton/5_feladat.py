lista = []
lista[0] = min
szam = int(input("adj meg egy pozitív számot"))
while szam >= 0:
    lista.append(szam)
    szam = int(input("adj meg egy pozitív számot"))
def min(lista):
    min = lista[0]
    for item in lista:
        if item < min:
            min = item
    return min
print("A lista legkisseb eleme:" + min(lista))