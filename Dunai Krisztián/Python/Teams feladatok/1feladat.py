szamok = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
paros_szamok(szamok)
[2, 4, 6, 8, 10]


def paros_szamok(szamlista):
    parosak = []
for szam in szamlista:
    if szam % 2 == 0:
        parosak.append(szam)
        return parosak
