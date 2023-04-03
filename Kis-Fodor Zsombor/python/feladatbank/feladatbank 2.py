'''
2. Készíts egy függvényt, amely egy adott számlistát vár bemenetként
majd visszaadja a listában található legnagyobb számot.
'''

szamlista = []
szam = None

while szam != '':
    szam = input('adjon meg egy számot')
    if szam != '':
        szamlista.append(int(szam))

legnagyobb = szamlista[0]

for szamok in szamlista:
    if szamok > legnagyobb:
        legnagyobb = szamok

print('a legnagyobb szám az:',legnagyobb)