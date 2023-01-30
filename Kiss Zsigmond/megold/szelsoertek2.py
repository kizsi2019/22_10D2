lista = []
szo = input("Adj meg egy szót! ")
while szo !='':
    lista.append(szo)
    szo = input("Adj meg egy szót! ")
print(lista)
min = lista[0]
max = lista[0]
for elem in lista:
    if len(elem) < len(min):
        min = elem
    if len(elem) > len(max):
        max = elem
print("A lista legkisebb eleme: ", min)
print("A lista legnagyobb eleme: ", max)
