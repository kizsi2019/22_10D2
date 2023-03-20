def szögek(x, *args):

    sex = None
    max = 0

    for szam in args:
        max += 1

    if max == 0:
        sex = 'négyzet'
        print(sex)
        return x * 4
    elif max == 1:
        sex = 'téglalap'
        print(sex)
        return  x + args[0] * 2
    elif max == 2:
        sex = 'háromszög'
        print(sex)
        return x +args[0] + args[1]
    else:
        sex = 'sokszög'
        print(sex)
        return x + szam

print(szögek(1))
print(szögek(1,2))
print(szögek(1,2,3))
print(szögek(1,2,3,4))