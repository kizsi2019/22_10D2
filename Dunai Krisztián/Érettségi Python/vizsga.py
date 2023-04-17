def sikeres_vizsga(pontszam):
    return pontszam >= 60

while True:
    nev = input("Add meg a vizsgázó nevét!\n")
    if nev == "":
        break
    pontszam = int(input("Add meg a pontszámát!\n"))
    if sikeres_vizsga(pontszam):
        print(nev, "vizsgája sikeres.")
    else:
        print(nev, "vizsgája sikertelen.")