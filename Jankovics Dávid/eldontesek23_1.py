szo = "macsek"
szo2 =input('adj meg egy betüt')

talalat = False
index = 0

while szo2 != "":
    szo2 =input('adj meg egy betüt')

while index < len(szo) and not talalat:
    if szo2 == szo[index]:
        talalat = True
    index = index +1


if talalat:
    print('szép volt faszfej')
else:
    print('nem volt szép faszfej')
print(szo)f
