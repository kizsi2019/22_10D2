diak = None
pontszam = 0
pontszamhatar = 48
atment = True

while diak !='':
    diak = input("Add meg a vizsgázó nevét!")
    if diak !='':
        pontszam=int(input("Add meg a pontszámát!"))
        if pontszam == pontszamhatar or pontszam > pontszamhatar:
            print(diak, "vizsgája sikeres")
        else:
            print(diak,"Vizsgája sikertelen")