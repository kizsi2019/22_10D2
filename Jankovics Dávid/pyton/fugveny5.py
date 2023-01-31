def legkisebb_szam():
    list = []
    adott_szam = 0
    while adott_szam >= 0:
        adott_szam = int(input('tököm'))
        if adott_szam > 0:
            list.append(adott_szam)

    min = list[0]

    for szamok in list:
        if szamok < min:
            min = szamok
    return min


print(legkisebb_szam())