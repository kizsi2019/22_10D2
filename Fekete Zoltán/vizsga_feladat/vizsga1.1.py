def vizsga(pontszam):
    if pontszam >= 48:
        return True
    else:
        return False

nev = None

while nev != "":
    nev = input("Add meg a vizsgázó nevét!")
    if nev:
        pontszam = int(input("Add meg a pontszámát!"))
        if vizsga(pontszam):
            print(nev, "vizsgája sikeres.")
        else:
            print(nev, "vizsgája sikertelen.")
