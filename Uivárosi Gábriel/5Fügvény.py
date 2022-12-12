def legkissebb():
    list = []

    T = False
    while T == False:
       be = int(input("Számot!!"))
       if be < 0:
           T = True
       else:
           list.append(be)
    kiss = list[0]
    for szam in list:
        if szam < kiss:
            kiss = szam
    print(kiss)




legkissebb()

