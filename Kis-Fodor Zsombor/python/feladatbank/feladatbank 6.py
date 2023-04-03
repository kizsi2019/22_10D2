'''
6. Készíts egy függvényt, amely egy adott számlistát vár bemenetként
majd visszaadja a listában található legkisebb és legnagyobb szám közötti különbséget.
'''

szamlista = []
szam = None

while szam != '':
    szam = input('adjon meg egy számot')
    if szam != '':
        szamlista.append(int(szam))

legkisebb = szamlista[0]
legnagyobb = szamlista [0]