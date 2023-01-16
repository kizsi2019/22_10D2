for i in range(3):
    szo = input("Ajd meg 3 szót")
    list.append(szo)

def eljaras(list):
    min = list[0]
    max = list[0]
    for i in list:
        if len(szo) < len(min):
            min = szo
        if len(szo) > len(max):
            max= szo
    print(list)
    print("A legkisebb szó a listában", min)
    print("A legnagyobb szó a listában", max)
eljaras(list)