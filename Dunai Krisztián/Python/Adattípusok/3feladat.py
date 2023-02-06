import random

lista = [[random.randint(-5, 5) for j in range(3)] for i in range(5)]

def print_list(lst):
    for row in lst:
        print(row)

print("Eredeti lista:")
print_list(lista)

lista = [list(filter(lambda x: x >= 0, row)) for row in lista]

print("A negatív számok törölt lista:")
print_list(lista)
