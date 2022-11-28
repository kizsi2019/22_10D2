szavak = ['Elemér', 'Emma', 'ajtó', 'róka', 'egér']
szavak_szurve = []
index = 0
for szo in szavak:
    if szo[0] == 'E' or szo[0] == 'e':
        szavak_szurve.append(szo)
        index = index + 1
print("A megfelelő szavak száma:", index)
print("A megfelelő szavak:", szavak_szurve )
