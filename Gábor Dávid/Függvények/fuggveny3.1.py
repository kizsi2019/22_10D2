def harommal_oszthatok(x, *args):
    darab = 0
    i = 0
    while i < len(args):
        if args[i] % 3 == 0:
            darab = darab + 1
        i = i + 1
    return darab
print(harommal_oszthatok(2,12,3,6,9))