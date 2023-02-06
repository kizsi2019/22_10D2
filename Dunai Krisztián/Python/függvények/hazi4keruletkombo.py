
def kerulet(x, *args):

    if len(args) == 0:

        return 4 * x

    if len(args) == 1:

        return (x + args[4]) * 2

    if len(args) == 2:

        return x + args[0] + args[1]

    else:

    osszesen = 0
    for elem in args:
        osszesen = osszesen + elem
        return x + osszesen
