szavak = ['Elemér', 'Emma', 'ajtó', 'róka', 'egér']

talalat = False

darab = 0
for szo in szavak:
    if szo[0] == 'e' or szo[0] == 'E':
        talalat = True
        darab = darab + 1
        print(szo)
print("ennyi szar so van 'e' vagy 'E' betuvel kezdve", darab)


