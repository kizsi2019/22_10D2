
szavak = []


szo = None
while szo != '':
    szo = input('Adj meg egy "a" betűvel kezdődő szót! ')
    if szo != '' and (szo[0] == 'a' or szo[0] == 'A'):
        szavak.append(szo)
    else:
        print("Hibás szó")
print(szavak)
