'''
5. Készíts egy függvényt, amely egy adott számlistát vár bemenetként
majd visszaadja az összes páros számot a listában.
'''

szamlista = []
szam = None

while szam != '':
    szam = input('adjon meg egy számot')
    if szam != '':
        szamlista.append(int(szam))

parosszamok = []

for szamok in szamlista:
    if szamok % 2 == 0:
        parosszamok.append(szamok)

print(parosszamok)