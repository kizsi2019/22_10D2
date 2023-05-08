def vizsga(x):
    if x >= 48:
        return True
    else:
        return False
Név = None
while Név != "":
    Név = input("Vizsgázó neve?")

    if Név != "":
        Pontszám = int(input("Elért pontszám"))
        if vizsga(Pontszám):
            print(Név, "vizsgája sikeres.")
        else:
            print(Név, "vizsgája sikertelen.")

