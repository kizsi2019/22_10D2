def kerölet(x, *args):
    list = []
    list.append(x)
    szög = 0
    for szam in args:
        if szam > 0:
            szög = szög + 1
            list.append(szam)
    if szög == 0:
        keruletszam = x*4
        print("az ön nényszöge kerülete: ", keruletszam )
    elif szög == 1:
        ösze = 0
        for oldal in list:

            ösze = ösze + oldal
        keruletszam = ösze*2


        print("az ön téglalapja kerülete:", keruletszam)
    elif szög == 2:
        keruletszam = 0
        for oldal in list:
            keruletszam = keruletszam + oldal
        print("az ön háromszöge kerülete:", keruletszam)
    else:
        keruletszam = 0
        for oldal in list:
            keruletszam = keruletszam + oldal
        print("az ön sokkszöge kerülete",keruletszam)








kerölet(4)
kerölet(4, 5)
kerölet(4, 5, 6)
kerölet(4, 5, 6, 7)