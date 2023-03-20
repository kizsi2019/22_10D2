import random

def fesul_lista(lista):
    return [szam for szam in lista if szam >= 0]

lista = [[random.randint(-5, 5) for x in range(3)] for y in range(5)]
print("Eredeti lista:")
for elem in lista:
    print(elem)

lista = [fesul_lista(sor) for sor in lista]
print("\nFésült lista:")
for elem in lista:
    print(elem)