def szögek(x, *plusz, sex = ''):

    max = 0

    for szam in plusz:
        max += 1
    if max == 0:
        sex = 'négyzet'
    elif max == 1:
        sex = 'téglalap'
    elif max == 2:
        sex = 'háromszög'
    else:
        sex= 'sokszög'

    return sex


print(szögek(1,2,3))
