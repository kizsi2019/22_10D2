lista = [2, 4, 5, 9, 11, 14, 15]

talalat = False
index = 0

while index < len(lista) and not talalat:
    if lista[index] % 3 == 0:
        talalat = True
    index = index + 1
if talalat:
    print('Van a listában hárommal osztható szám!')


