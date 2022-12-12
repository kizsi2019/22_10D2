def paros_e(x, *args):
    talalat = False
    i = 0
    while i <len(args) and not talalat:
        if args[1] % 2 == 0:
            talalat = True
            return talalat
        else:
            return talalat
    i = i + 1

print(paros_e(5,1,3))
