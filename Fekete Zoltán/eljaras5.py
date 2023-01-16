szavak = []
for i in range(3):
    szo = input("Adj meg egy szót!")
    szavak.append(szo)
min = szavak[0]
for szo in szavak:
    if len(szo) < len(min):
        min = szo
    print("Ez volt a legrövidebb szó: ", min)