def paros_e(x, *args):
    talalat = False
    i = 0
    while i <len(args) and not talalat:
        if args[i] % 2 == 0:
            talalat = True
            return talalat
        else:
            return talalat
    i = i +1

print(paros_e(2,1,3))