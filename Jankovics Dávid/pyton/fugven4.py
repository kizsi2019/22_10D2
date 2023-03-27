def kerulet(x, *args):
    if len(args) == 0:
        return 4 * x
    if len(args) == 1:
        ker1 = 0
        for szam in args:
            ker1= ker1 + szam
            return 2 * x + 2 * ker1
    if len(args) == 2:
        ker1 = 0
        for szam in args:
            ker1= ker1 + szam
            return x + ker1
        else:
            ker1 = 0
            for szam in args:
                ker1 = ker1 + szam
            return x + ker1

print(kerulet(2, 3, 6))
