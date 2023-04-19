óra = input('hány óra van most?')
óra = int(óra)
if óra >= 8 and óra < 16:
    print('A bolt nyitva van.')
    eddig = 16 - óra
    print('ennyi órád van odaérni:', eddig)
else:
    print('a bolt zárva van')
