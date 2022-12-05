lista = []
for i in range (3):
    szo = input("Adj meg egy szót")
    lista.append(szo)
def legrovidebb(lista):
    min = lista[0]
    for elem in lista:
        if len elem < (len)min