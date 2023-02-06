def harommal_oszthato(list, szam = False):
    for numbers in list:
        if numbers % 3 == 0:
            szam = True
    return szam
list = []
megadott_szam = 0
while megadott_szam >= 0:
    megadott_szam = int(input('Adj meg egy számot!'))
    if megadott_szam > 0:
        list.append(megadott_szam)


print(harommal_oszthato(list))