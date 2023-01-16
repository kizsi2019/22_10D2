def harommal_oszthato(x, *args):
    darab = 0
    i = 0
    while i <len(args):
        if args[i] % 3 == 0:
            darab = darab + 1
        i = i + 1
    return darab
print(harommal_oszthato(22,12,32,33,6,9,69))