def paros(x,y, szam = None):
    if x % 2 == 0 or y % 2 == 0:
        szam = True
    else:
        szam = False

    return

x = int(input('x'))
y = int(input('y'))

print(paros(y,x))