szavak = ['alma', 'barack', 'Attila', 'kávé', 'szekrény', 'asztal']

index = 0

for szo in szavak:
    if szo[0] == 'a' or szo[0] == 'A':
        index += 1

print(f'ennyi a/A betűvel kezdődő szám van {index}')