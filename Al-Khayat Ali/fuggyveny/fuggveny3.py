def harommal_oszhatok(list):
    darab = 0
    for elem in list:
        if int(elem) % 3 == 0:
            darab = darab + 1
        return darab
    list = []
    szam = input=("adj meg egy számot!")
    while int(szam) >= 0:
        list.append(szam)
        szam = input("adj meg egy szamot!")
    print(harommal_oszhatok(list))
