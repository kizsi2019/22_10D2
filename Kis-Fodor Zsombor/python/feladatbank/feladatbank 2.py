'''
2. Készíts egy függvényt, amely egy adott számlistát vár bemenetként
majd visszaadja a listában található legnagyobb számot.
'''

import random
szamlista = []
szam = None

# funkció
def Szam():
    legnagyobb = szamlista[0]

    for szamok in szamlista:
        if szamok > legnagyobb:
            legnagyobb = szamok

    print('a legnagyobb szám az:', legnagyobb)

# manuális input
while szam != '':
    szam = input('adjon meg egy számot')
    if szam != '':
        szamlista.append(int(szam))

# random input

# előre megadott infó

# funkció meghívása
Szam()