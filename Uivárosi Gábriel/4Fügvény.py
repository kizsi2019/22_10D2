
def kerulet():
    list = []
    be = 0
    for köt in range(4):
        be = int(input("Kötelező Oldal értéket"))
        ker = ker + be
        szög = szög + 1
    while be != 0:
        be = int(input("Opcionális Oldal értéket, Irj 0 ha befejezted"))
        if be != 0:
            list.append(be)
    ker = 0
    szög = 0
    for szam in list:
        ker = ker +szam
        szög = szög+1
    print("Az ön", szög, "szög e kerülete:", ker)
kerulet()


    
    

