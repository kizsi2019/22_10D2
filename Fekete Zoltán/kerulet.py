def sikidomok(x, *args):
    if len(args) == 0:
        sikidom = "Négyzet"
        return 4 * x, sikidom
    if len(args) == 1:
        sikidom = "Téglalap"
        return (x + args[0]) * 2, sikidom
    if len(args) == 2:
        sikidom = "Háromszög"
        return x + args[0] + args[1], sikidom
    else:
        elemek = 0
        for elem in args:
            elemek = elemek + elem
        sikidom = "Sokszög"
        return x + elemek, sikidom
print(sikidomok(1))
print(sikidomok(2, 4))
print(sikidomok(2, 4, 6))
print(sikidomok(2, 4, 6, 8))
