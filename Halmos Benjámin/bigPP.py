lista = []
szo1 = input("adjon meg egy szót")


while szo1 != "":
    lista.append(szo1)
    szo1 = input("adjon meg egy szót")

min = lista[0]
max = lista[0]

for elem in lista:
    if len(elem) < len(min):
        elem = min

    if len(elem) > len(max):
        elem = max


print(lista)
print("a legrövidebb szó:", min)
print("a leghosszabb szó:", max)
