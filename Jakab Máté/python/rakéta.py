szam =input('Hány óra van a visszaszámlálásig?')
szam = int(szam)
print(f'Vissza számlálás: {int(szam)}')


for i in range(szam):
    szo = input('Fel kell fügeszteni a visszaszámlálást(i/n)?')
    if szo == 'n':
        szam -= 1
        print(f'Vissza számlálás: {int(szam)}')
    if szo == 'i':
        break