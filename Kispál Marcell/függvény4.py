def kerulet(x, *args):
    idom = None
    if len(args)== 0:
    idom = négyzet
        return x * x
    if len(args)== 1:
    idom = téglalap
	    return (x   * args[0]) * 2
    if len(args)== 2:
    idom = háromszög
        return x + args [0] +args[1]
    else:
        idom = sokszög
        osszesen = 0
        for elem in args:
            osszesen = osszesen + elem
        return idom, x + osszesen
idom = None
print(idom)
print(kerulet(2))
print(kerulet(2,3))
print(kerulet(2,3,4))
print(kerulet(2,3,4,5))
