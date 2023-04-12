def paros_szamok(szamlista):
    parosak = []
    for szam in szamlista:
        if szam % 2 == 0:
            parosak.append(szam)
    return parosak

szamok = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
parosak = paros_szamok(szamok)
print(parosak)

