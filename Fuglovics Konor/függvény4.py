def kerulet(x, *args):
    if len(args) == 0:
        return 4 * x
    elif len(args) == 1:
        return (x + args[0]) * 2
    elif len(args) == 2:
        return x + args[0] + args[1]
    else:
        total = 0
        for b in args:
            total += b
        return x + total


print(kerulet(2))
print(kerulet(2, 3))
print(kerulet(2, 3, 4))
print(kerulet(2, 3, 4, 5))
