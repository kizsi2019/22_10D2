def atlag(szamok):
    osszeg = sum(szamok)
    db = len(szamok)
    if db == 0:
        return 0
    else:
        return osszeg / db

szamok = input("Adjon meg egy számlistát vesszővel elválasztva: ")
szamok = [int(szam) for szam in szamok.split(",")]

print("A számok átlaga: ", atlag(szamok))
