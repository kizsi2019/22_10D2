szamok = []
szam = int(input("Adj meg számokat!"))
while szam > 0:
    szamok.append(szam)
    szam = int(input("Adj meg egy számot!"))
def min(szamok):
    min = szamok[0]
    for elem in szamok:
        if elem < min:
            min = elem
    return min