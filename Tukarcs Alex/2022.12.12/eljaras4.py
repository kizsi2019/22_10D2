for i in range(3):
    szo = input("adj meg 3 szót")
    list.append(szo)

def eljaras(list):
    min = list[0]
    max = list[0]
    for i in list:
        if len(elem) < len(min):
            min = elem
        if len(elem) > len(max):
            max = elem
    print(list)
    print("A legkisebb szó a listában", min)
    print("A legnagyobb szó a listában", max)
eljaras(list)