def sikeres_vizsga(pontszam):
    if pontszam >= 48:
        return True
    else:
        return False

while True:
    nev = input("Add meg a vizsgázó nevét! ")
    if nev == "":
        break
    pontszam = int(input("Add meg a pontszámát! "))
    if sikeres_vizsga(pontszam):
        print(nev + " vizsgája sikeres.")
    else:
        print(nev + " vizsgája sikertelen.")
