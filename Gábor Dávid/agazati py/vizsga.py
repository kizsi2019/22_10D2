def sikeres_vizsga(pontszam):
    if pontszam >= 60:
        return True
    else:
        return False

while True:
    vizsgazo = input("Add meg a vizsgázó nevét! ")
    if not vizsgazo:
        break
    pontszam = int(input("Add meg a pontszámát! "))
    if sikeres_vizsga(pontszam):
        print(f"{vizsgazo} vizsgája sikeres.")
    else:
        print(f"{vizsgazo} vizsgája sikertelen.")
