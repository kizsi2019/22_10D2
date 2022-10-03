'''
for i in range(1, 41):
    if i % 3 == 0:
        print(i)

szavak = ['ajtó', 'tojás', 'Ottó', 'Tamás', 'tép', 'tesla']

for szo in szavak:
    if szo[0] == "T" or szo[0] == "t":
        print(szo)
   '''
szavak = ['ajtó', 'tojás', 'Ottó', 'Tamás', 'tép', 'tesla']
szo_lista = []
for szo in szavak:
    if szo[0] == "T" or szo[0] == "t":
        szo_lista.append(szo)
print(szo_lista)