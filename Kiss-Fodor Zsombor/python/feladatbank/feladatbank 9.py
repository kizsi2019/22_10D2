'''
9. Készíts egy függvényt, amely egy adott számlistát vár bemenetként
majd visszaadja a lista elemeit megfordítva.
'''

import random
szamlista = []
szam = None

# funkció
def Visszafele():

    szamlista.reverse()
    print('ezek a lista elemei visszafele:', szamlista)

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
# funkció meghívása
Visszafele()