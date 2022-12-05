def legrovidebb():

    szavak = []

    db = 0
    while db < 3:
        szo = input("adj meg egy szót")
        db += 1
        szavak.append(szo)

    min = szavak[0]
    max = szavak[0]

    for szo in szavak:
        if szo > max:
            max = szo
        if szo < min:
            min = szo

    print(f'a legrövidebb szó {min}')

legrovidebb()