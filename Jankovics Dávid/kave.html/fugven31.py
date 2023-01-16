def harommal_oszthato(x, *args):
    darab = 0
    i = 0
    while i < len(args):
        if args[i] % 3 == 0:
            darab = darab +1
        i = i +1
    return darab

print(harommal_oszthato(1,2,3,4,5,6,7,8,6,5,4,4,6,7,8,8,7,5,4,5,7,8,6,67,45,745,754,75,7,457,47,47,))