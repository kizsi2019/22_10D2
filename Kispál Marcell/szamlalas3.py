szavak = ['Elemér', 'Emma', 'ajtó', 'róka', 'egér']

darab = 0
for szo in szavak:
    if szo[0] == "E" or szo[0] == "e":
        darab = darab + 1
        print(szo)
print("ennyi 'e' vagy 'E' betűvel kezdődő szó van: ", darab)
