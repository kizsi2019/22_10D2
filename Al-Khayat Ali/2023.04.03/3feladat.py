def szavak_szama(szoveg):

    szavak = szoveg.split()
    return len(szavak)

szoveghez = input("adjon meg egy mondatot!")
szavak_szama = szavak_szama(szoveghez)
print(f"a mondathoz {szavak_szama} szo van")