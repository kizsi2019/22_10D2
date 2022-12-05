def kerulet():
    list = []
    be = 1
    while be != 0:
        be = int(input("szám"))
        if be != 0:
            list.append(be)
    ker = 1
    szög = 0
    for szam in list:
        ker = ker*szam
        szög = szög+1
    print("Az ön", szög, "szög e kerülete:", ker)
kerulet()


