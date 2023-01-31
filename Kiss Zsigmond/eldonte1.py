import random
lista = []
talalat = False
index = 0
for i in range(5):
    veletlen_szam = random.randint(1,7)
    lista.append(veletlen_szam)
szam = int(input("Adj meg egy számot 1 és 7 között!"))
while index < len(lista) and not talalat:
    if szam == lista[index]:
        talalat = True
    index = index + 1
print(lista)
if talalat:
    print("Van talalat!")
else:
    print("Nincs talalat!")