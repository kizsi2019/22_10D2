

def harommal_oszthatok(x, *args):
    har = 0
    if x % 3 == 0:
        har = har + 1
    for szam in args:
        if szam % 3 == 0:
            har = har + 1
    print(har)
harommal_oszthatok(2, 3, 4, 5, 6, 23, 21, 22, 9)
