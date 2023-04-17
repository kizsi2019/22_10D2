def szavak_szama(szoveg):
    szavak = szoveg.split()
    szavak_szama = len(szavak)
    return szavak_szama

szoveg = "Ez egy példa mondat, amelyben szavakat kell számlálni."
szavak_szama = szavak_szama(szoveg)
print(szavak_szama)