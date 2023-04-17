szamok = []

def legkisebb(szamok):
    megadott = int(input("Adj meg számokat!"))
    szamok.append(megadott)
    while True:
        megadott = int(input("Adj meg még számokat! Ha nem akarsz több számot megadni, adj meg egy negatív számot!"))
        szamok.append(megadott)
        if megadott < 0:
            print("Vége a megadásnak!")
            szamok.pop()
            break

    min = szamok[0]
    for szam in szamok:
        if szam < min:
            min = szam
    return legkisebb
print(legkisebb(szamok))