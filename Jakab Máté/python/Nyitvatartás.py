zaras = 16

szam = input('Hány óra van most')
if int(szam) < zaras:
    print('A bolt nyitva van')
    print(f'Ennyi óra van oraérni {16-int(szam)}')

else:
    print(f'A bolt zárva van.')