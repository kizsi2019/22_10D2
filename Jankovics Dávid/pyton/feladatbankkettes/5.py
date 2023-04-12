
def szamok_atlag(szamlista):
    osszeg = sum(szamlista)
    atlag = osszeg / len(szamlista)
    return atlag

szamok = [3, 7, 1, 10, 8, 2, 9]
atlag = szamok_atlag(szamok)
print(atlag)