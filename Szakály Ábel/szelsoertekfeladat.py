list = []
szo = input('Adj meg szavakat!')
while szo != "":
    list.append(szo)
    szo = input('Adj meg szavakat!')
min = list[0]
max = list[0]
for elem in list:
    if len(elem) < len(min):
        min = elem
    if len(elem) > len(max):
        max = elem
print(list)
print('A legkisebb szó a listában: ', min)
print('A legnagyobb szó a listában: ', max)
