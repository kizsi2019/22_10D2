def szögek(x, *plusz, sex = ''):

    max = 0
    
    for szam in plusz:
        max += 1
    if max == 0:
        sex = '0'
    elif max == 1:
        sex = '1'
    elif max == 2:
        sex = '2'
    else:
        sex= '3'

    return sex


print(szögek(1,2,3))
