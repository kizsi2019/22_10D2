felhasznalo = ""
jelszo = ""

while felhasznalo != "Bori99" or jelszo != "Szivecske<3":
    felhasznalo = input("Adja meg a felhasználónevét!")
    jelszo = input("Adja meg a jelszavát!")
    if felhasznalo == "Bori99" and jelszo == "Szivecske<3":
        print("Belépés engedélyezve.")
    else:
        print("Belépés megtagadva.")