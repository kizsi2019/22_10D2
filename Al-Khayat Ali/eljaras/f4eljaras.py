list = []

for i in range(3):
    szo = input("adj meg 3 szot!")
    list.append(szo)

def eljaras(list):
    min = list[0]
    max = list[0]
    for elem in list:
        if len(elem) < len(min):
            min = elem
        if len(elem) > len(max):
            max = elem
    print(list)
    print('a legkissebb szo a lisaban: ', min)
    print('a legnagyobb szo a listaban', max)
eljaras(list)

