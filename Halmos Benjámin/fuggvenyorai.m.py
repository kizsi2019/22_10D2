#feladat1
'''
def osszegzo(x,y):
    return x+y
print(osszegzo(3,5))
'''


#feladat2
'''
def paros_e(x, *args):
    talalat = False
    i = 0
    while i < len(args) and not talalat:
        if args[1] % 2 == 0:
            talalat = True
            return talalat
        else:
            return talalat
    i = i + 1
print(paros_e(5,1,3,2))
'''

#3.1

def harom_e(x, *args):
    darab = 0
    i = 0
        while i < len(args) and not talalat:
            if args[1] % 3 == 0:
                darab = darab + 1
            return darab
        i = i + 1
print(harom_e(5,1,3,2,9 ,12,6,66))