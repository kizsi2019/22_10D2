def sikeres_vizsga(pontszam):
    return pontszam >= 48

while True:
    nev = input("Add meg a vizsgázó nevét! ")
    if nev == "":
        break
    pontszam = int(input("Add meg a pontszámát! "))
    if sikeres_vizsga(pontszam):
        print(nev, "vizsgája sikeres.")
    else:
        print(nev, "vizsgája sikertelen.")