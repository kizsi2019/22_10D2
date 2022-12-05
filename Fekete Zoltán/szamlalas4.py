szavak = ['Elemér', 'Emma', 'ajtó', 'róka', 'egér']

print('Ennyi szó van összesen: ', len(szavak[0]))
darab = 0
joszavak = []
for szo in szavak:
    if szo[0] == 'E' or szo[0] == 'e':
        darab = darab + 1
        joszavak.append(szo)
print('Ezek a jó szavak: ', joszavak)
print("Ennyi 'e' vagy 'E' betűvel kezdődő szó van: ", darab)