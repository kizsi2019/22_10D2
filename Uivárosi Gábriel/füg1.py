'''
def oszegzo(x, y):
    return x + y


print(oszegzo(9231239999, -1213123143))
'''
list = [1, 6, 5]
def paros_E(x, *args):
    T = False
    for szam in list:
        if szam % 2 == 0:
            T = True
    if T:
        print("PÁÁÁROS")
paros_E(list)


