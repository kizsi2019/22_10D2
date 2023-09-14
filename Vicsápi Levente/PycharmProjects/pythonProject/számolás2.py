szavak = ['Emma', 'róka', 'egér', 'eke']

hvg = 0

for szo in szavak:
    if szo[0] == 'e' or szo[0] == 'E':
        hvg += 1
        print(szo)

print(f'ennyi e vagy E betűvel kezdődő szó van a listában {hvg}')
