diak = None
pontszamdiak = 0
atment = True

while diak != "":
    diak = input("Add meg a vizsgázó nevét!")
    if diak != "":
        pontszamdiak = int(input("Add meg a pontszámát! "))
        if pontszamdiak >= 48:
            atment = True
        else:
            atment = False

        if atment == True:
            print(diak, "vizsgája sikeres.")
        else:
            print(diak, "vizsgája sikertelen.")