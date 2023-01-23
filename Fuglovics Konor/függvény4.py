def kerulet(x, *args):
    a = None
    if len(args) == 0:
        a = "Négyzet"
        return a, 4 * x
    elif len(args) == 1:
        a = "Téglalap"
        return a, (x + args[0]) * 2
    elif len(args) == 2:
        a = "Háromszög"
        return a, x + args[0] + args[1]
    else:
        total = 0
        for b in args:
            total += b
        return x + total

a = None
print(a)
print(kerulet(2))
print(kerulet(2, 3))
print(kerulet(2, 3, 4))
print(kerulet(2, 3, 4, 5))