def szögek(x, *plusz, szam2 = ''):

    max = 0

    for szam in plusz:
        max += 1
    if max == 0:
        szam2 = '0'
    elif max == 1:
        szam2 = '1'
    elif max == 2:
        szam2 = '2'
    else:
        szam2= '3'

    return szam2


print(szögek(1,2,3))
