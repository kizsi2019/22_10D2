import random as Rando


def paros(*args):



    paros = []
    for szam in args:
        if szam % 2 == 0:
            paros.append(szam)
    return paros

'''
Elemek megadva
print(paros(2 ,10 ,3 ,1 ,6 ,7))
'''
'''
Bekérem felhasználótól
T = True
list = []
while T == True:
    inputtt = int(input("Számot!!"))
    if inputtt != 0:
        list.append(inputtt)
    else:
        T = False
for elem in list:
    print(paros(elem))
'''
for index in range(5):
    randdomm = Rando.randint[1, 290]

    print(paros(randdomm))



