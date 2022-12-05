F = False
def paros_e(*args):
    paros = args
    for szam in args:
        if szam % 2 == 0:
            F = True
    if F:
        print("Ez a szám páros.")
    else:
        print("Ez a szám páratlan.")

print(paros_e(4,3,1,4,2))