def legkisebb(list):
    min = list[0]
    for elem in list:
        if int(elem) < int(min):
            min = elem
    return min
list = []
szam = input("Adj meg egy számot! ")
while int(szam) >= 0:
    list.append(szam)
    szam = input("Adj meg egy számot! ")
print(legkisebb(list))
