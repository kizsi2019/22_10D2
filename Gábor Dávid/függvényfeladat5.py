def legkisebb():
    list = []
    szam = 0
    while szam >= 0:
        szam = int(input('...'))
        if szam > 0:
            list.append(szam)

    min = list[0]

    for i in list:
        if i < min:
            min = i
    return min


print(legkisebb())