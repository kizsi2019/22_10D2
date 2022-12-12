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

print(szamok)

def harommal_oszthato(szamok):
    oszthato = 0
    for szam in szamok:
        if szam % 3 == 0:
            oszthato = oszthato + 1
            print(oszthato)
harommal_oszthato(szamok)