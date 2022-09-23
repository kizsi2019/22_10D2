enter = False
namelist = []
sex = 3
nameask = None

while nameask != True:
    nameask = input('gib names')
    if nameask == '':
        enter = True
    else:
        namelist.append(nameask)
    sex -= 1
    if sex <= 0:
        enter = True
        print('you ran out of chances')

print(namelist)
