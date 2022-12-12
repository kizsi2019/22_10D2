'''
def oszegzo(x, y):
    return x + y


print(oszegzo(9231239999, -1213123143))
'''
def paros_E(x, *args):
    T = False
    if x % 2 == 0:
        T = True
    for szam in args:
        if szam % 2 == 0:
            T = True
    if T:
        print("PÁÁÁROS")
paros_E(1, 6, 5)


