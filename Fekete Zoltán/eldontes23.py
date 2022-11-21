szo = 'kocsi'
index = 0
talalat = False
van = 0
nincs = 0

betu = input('Adj meg egy betüt! Ha nem akarsz több betüt megadni, nyomd meg csak az ENTER-t!')
while betu != '':
    while index < len(szo) and not talalat:
        if szo[index] == betu:
            talalat = True
        index = index + 1
if talalat:
    print('Ez a betű létezik a szóban.')
    van = van + 1
    talalat = False
else:
    print('Ez a betű nem létezik a szóban.')
    nincs = nincs + 1

print('A szó ez volt:', szo)
print('Ennyi találat volt: ', van)
print('Ennyi hiba volt: ', nincs)