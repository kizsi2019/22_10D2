def legkisebb():
    list = []
    szam = 0
    while szam >= 0:
        szam = int(input('Adj meg egy pozitív számot owo!'))
        if szam > 0:
            list.append(szam)
    min = list[0]
    for numbers in list:
        if numbers < min:
            min = numbers
    return min


print(legkisebb())