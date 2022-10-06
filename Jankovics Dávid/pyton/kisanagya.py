szavak = []

szo = None
while szo != '':
    szo = input('adj meg egy a/A val kezdődő szavat! ')
    if szo != '' and (szo[0] == 'a' or szo[0] == 'A'):
        szavak.append(szo)

print(szavak)
