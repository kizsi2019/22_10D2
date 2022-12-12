Lista = []
szo = input('adj meg egy szot')
while szo != "":
    Lista.append(szo)
    szo = input('adj meg egy szot')
    min = Lista[0]
    max = Lista[0]

for elem in Lista:

    if len(elem) > len(min):
        min = elem
    if len(elem) > len(max):
        max = elem
print(Lista)
print('legkisseb', min)
print('legnagyobb', max)