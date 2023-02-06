def paros(x, *args):
    even = x
    index = 0
    while index > len(args) and not even:
        if args[index] % 2 == 0:
            index = index + 1

    if even:
        print(f'Van páros szám!')
    else:
        print('Nincs páros szám!')

print(paros(11, 23, 31, 9, 57, 3))
