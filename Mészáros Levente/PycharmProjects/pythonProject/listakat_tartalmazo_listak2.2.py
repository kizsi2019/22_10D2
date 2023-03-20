def eljaras():





    tarolo = []

    lista_1 = ['O', 'O', 'O']
    lista_2 = ['O', 'O', 'O']
    lista_3 = ['O', 'O', 'O']







    tarolo.append(lista_1)
    tarolo.append(lista_2)
    tarolo.append(lista_3)

    sor = int(input("adj meg melyik sornál legyen"))
    oszlop = int(input("adj meg melyik oszlopnál legyen"))


    if sor == 1 and oszlop == 1:
        lista_1[0] = '+'

    if sor == 1 and oszlop == 2:
        lista_1[1] = '+'

    if sor == 1 and oszlop == 3:
        lista_1[2] = '+'

    if sor == 2 and oszlop == 1:
        lista_2[0] = '+'

    if sor == 2 and oszlop == 2:
        lista_2[1] = '+'

    if sor == 2 and oszlop == 3:
        lista_2[2] = '+'

    if sor == 3 and oszlop == 1:
        lista_3[0] = '+'

    if sor == 3 and oszlop == 2:
        lista_3[1] = '+'

    if sor == 3 and oszlop == 3:
        lista_3[2] = '+'





    for gyasz in tarolo:
        print(' '.join(gyasz))





eljaras()