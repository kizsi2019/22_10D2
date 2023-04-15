'''
6. Készíts egy függvényt, amely egy adott számlistát vár bemenetként
majd visszaadja a listában található legkisebb és legnagyobb szám közötti különbséget.
'''

import random
szamlista = []
szam = None

# funkció
def Szamkulonbseg():
    legkisebb = szamlista[0]
    legnagyobb = szamlista[0]
    kulonbseg = 0

    for szamok in szamlista:
        if szamok > legnagyobb:
            legnagyobb = szamok
        if szamok < legkisebb:
            legkisebb = szamok
    kulonbseg = legnagyobb - legkisebb

    print('a legnagyobb szám az:', legnagyobb, 'a legkisebb pedig:', legkisebb, 'a különbségük pedig:', kulonbseg)

# manuális input
while szam != '':
    szam = input('adjon meg egy számot')
    if szam != '':
        szamlista.append(int(szam))
'''
# random input
for i in range(5):
    szam = random.randint(0,10)
    szamlista.append(int(szam))

# előre megadott infó
szam = [0,1,3,2,5,10]
for szam_tagok in szam:
    szamlista.append(szam_tagok)
'''
# funckió meghívása
Szamkulonbseg()