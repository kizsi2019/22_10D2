def harommal_oszthatok(list):
    darab = 0
    for elem in list:
        if int(elem) % 3 == 0:
            darab = darab + 1
    return darab
list = []
szam = input("Adj meg egy számot! ")
while int(szam) >= 0:
    list.append(szam)
    szam = input("Adj meg egy számot! ")
print(harommal_oszthatok(list))