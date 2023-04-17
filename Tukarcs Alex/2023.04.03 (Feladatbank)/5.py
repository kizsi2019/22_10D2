def paros_szamok():
    """
    Kér egy számlistát a felhasználótól, majd visszaadja az összes páros számot a listában.
    """
    szamok = input("Adja meg a számokat vesszővel elválasztva: ")
    szamok = [int(szam.strip()) for szam in szamok.split(",")]
    parosak = []
    for szam in szamok:
        if szam % 2 == 0:
            parosak.append(szam)
    return parosak

parosak = paros_szamok()
print(parosak)
