def sikeres(pontdiak):
    if pontdiak >= 48:
        return True
    else:
        return False

diak = None

while diak != "":
    diak = input("Add meg a vizsgázó nevét!")
    if diak:
        pontdiak = int(input("Add meg a pontszámát! "))

        if sikeres(pontdiak):
            print(diak, "vizsgája sikeres.")
        else:
            print(diak, "vizsgája sikertelen.")