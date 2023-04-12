def szavak_szama(szoveg):
    szavak = szoveg.split()
    return len(szavak)

mondat = "Ez egy példa mondat."
szavak_szama = szavak_szama(mondat)
print(szavak_szama)