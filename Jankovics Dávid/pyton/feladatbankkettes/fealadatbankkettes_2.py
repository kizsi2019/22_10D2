def legnagyobb_szam(szamlista):
    legnagyobb = szamlista[0]
    for szam in szamlista:
        if szam > legnagyobb:
            legnagyobb = szam
    return legnagyobb


szamok = [3, 7, 1, 10, 8, 2, 9]
legnagyobb = legnagyobb_szam(szamok)
print(legnagyobb)
