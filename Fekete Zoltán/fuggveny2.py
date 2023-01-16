def paros_e(x, *args):
    F = False
    ok = 0
    while ok < len(args) and not F:
        if args[ok] % 2 == 0:
            F = True
            return F
        else:
            return F
        ok = ok + 1


print(paros_e(4,4))