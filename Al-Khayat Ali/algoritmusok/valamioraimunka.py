lista = ['Kek', 'zold', 'piros', 'feher']
talalat = False
indexn = 0

talalat = False
index = 0
while infex < len(lista) and not talalat:
    if lista[index] == 'piros':
        talalat = true
    index = index + 1

if talalat:
    print('van a listadban piros, az indexe?', index-1)
else:
    print('nincs a listadban piros')