def paros_e(x,y, sus = None):
    if x % 2 == 0 or y % 2 == 0:
        sus = True
    else:
        sus = False

    return sus

x = int(input('x'))
y = int(input('y'))

print(paros_e(y,x))