def vizsgak(nev, pontszam):
    ok = True
    siker = "sikeres volt a vizsgája."
    sikertelen = nev, "sikertelen volt a vizsgája."
    nevek = []
    nev = input("Add meg a vizsgázó nevét!")
    pontszam = int(input("Add meg a vizsgázó pontszámát!"))
    if nev == "":
        ok = False
        nevek.append(nev)
    if pontszam > 48:
        return siker
    else:
        return sikertelen

print(vizsgak("Fekete Zoltán", "10" ))