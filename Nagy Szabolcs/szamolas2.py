szavak = ['alma', 'barack', 'Attila', 'kávé', 'szekrény', 'asztal']
szavak_szurve = []
index = 0
for szo in szavak:
    if szo[0] == 'a' or szo[0] == 'A':
        szavak_szurve.append(szo)
        index = index + 1
print("A megfelelő szavak száma:", index)
print("A megfelelő szavak:", szavak_szurve )
