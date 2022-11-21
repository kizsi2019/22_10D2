szo = 'kocsi'
index = 0
talalat = False

betu = input('Adj meg egy betüt!')
while index < len(szo) and not talalat:
    if szo[index] == betu:
        talalat = True
    index = index + 1
if talalat:
    print('Ez a betű létezik a szóban.')
else:
    print('Ez a betű nem létezik a szóban.')
print('A szó ez volt:', szo)
