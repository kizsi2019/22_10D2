def paros_szamok(szamlista):
    parosak = []
    for szam in szamlista:
        if szam % 2 == 0:
            parosak.append(szam)
    return parosak


szamok = [3, 7, 1, 10, 8, 2, 9]
parosak = paros_szamok(szamok)
print(parosak)
