

def harommal_oszthatok():
    list = []

    T = False
    while T == False:
        be = int(input("Számot!!"))
        if be < 0:
            T = True
        else:
            list.append(be)
    har = 0
    for szam in list:
        if szam % 3 == 0:
            har = har + 1
    print(har)
harommal_oszthatok()

