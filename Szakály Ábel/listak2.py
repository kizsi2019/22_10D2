szavak = []
szo = None

while szo !='':
    szo = input('Adj meg egy a betűvel kezdődő szót')

    if szo != '' and szo[0] =='a':
       szavak.append(szo)
       print("Helyes!")
    elif szo != '' and szo[0] =='A':
        szavak.append(szo)
        print("Helyes")
    else:
        print('Ez a szó nem a betűvel kezdődik')

print(szavak)


