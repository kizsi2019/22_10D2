''' Egyenlőtlenhez
def kerulet():
    list = []
    be = 1
    while be != 0:
        be = int(input("Oldal értéket, Irj 0 ha befejezted"))
        if be != 0:
            list.append(be)
    ker = 0
    szög = 0
    for szam in list:
        ker = ker +szam
        szög = szög+1
    print("Az ön", szög, "szög e kerülete:", ker)
kerulet()
'''
def kerulet2(x, y):
    p = 0
    p = x * y
    return p
    
    

print(kerulet2(300, 4))      
