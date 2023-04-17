def szavak_szama(mondat):

    szavak = mondathoz.split()
    return len(szavak)

mondathoz = input("Kérem, adjon meg egy mondatot: ")
szavak_szama = szavak_szama(mondathoz)
print(f"A mondatban {szavak_szama} darab szó van.")
