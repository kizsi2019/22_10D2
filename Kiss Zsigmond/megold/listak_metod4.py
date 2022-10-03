import random
lista =[]
lista2 = []

for i in range(10):
    szam = random.randint(1,3)
    lista.append(szam)
print(lista)
szam2 = int(input("Adj meg egy számot 1 és 3 között!"))
print(szam2)
for i in lista:
    #print("index ", i)
    if i != szam2:
        print(i, end=' ')




