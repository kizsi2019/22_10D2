import random
lista = []

for i in range(10):
    szam = random.randint(1,3)
    lista.append(szam)
print(lista)
szam2 = int(input("Adj meg egy szá,ot 1 és 3 között!"))

for i in lista: