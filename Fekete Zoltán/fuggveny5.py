szamok = []
megadott = int(input("Adj meg számokat!"))
szamok.append(megadott)
while True:
    megadott = int(input("Adj meg még számokat! Ha nem akarsz több számot megadni, adj meg egy negatív számot!"))
    szamok.append(megadott)
    if megadott < 0:
        print("Vége a megadásnak!")
        szamok.pop()
        break


def legkisebb(szamok):
    min = szamok[0]
    for szam in szamok:
        if szam < min:
            min = szam
print(legkisebb(szamok))