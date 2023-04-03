'''
4. Készíts egy függvényt, amely egy adott számlistát vár bemenetként
majd visszaadja a listában található számok átlagát.
'''

szamlista = []
szam = None

while szam != '':
    szam = input('adjon meg egy számot')
    if szam != '':
        szamlista.append(int(szam))

atlag = 0

for szamok in szamlista:
    atlag += szamok

atlag = atlag / len(szamlista)

print('a szamok átlaga:', atlag)