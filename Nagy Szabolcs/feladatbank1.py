'''1. Készíts egy függvényt, amely egy adott számlistát vár bemenetként,
 majd visszaadja az összes páros számot a listában.'''

szam = None
szamok = []
parosszam = []


while szam != '':
    szam = input("Adj meg egy számot")
    if szam !='':
         szamok.append(int(szam))

for szam in szamok:
    if szam % 2 == 0:
        parosszam.append(szam)


print(parosszam)




