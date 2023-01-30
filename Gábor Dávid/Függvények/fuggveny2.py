def paros_e(x, y):
    szam = x+y
    while szam % 2:
        return True
    else:
        return False
print(paros_e(1,4))