
list = [2, 3, 4, 5, 6, 23, 21, 22, 9]
def harommal_oszthatok(x, *args):
    har = 0
    for szam in list:
        if szam % 3 == 0:
            har = har + 1
    print(har)
harommal_oszthatok(list)



