felhasznalo = "bori99"
jelszo = "Szivecske<3"

megadottfalhasznalo = input("Kérem adja meg a felhasználónevet")
megadottjelszo = input("Kérem adja meg a jelszót")

while felhasznalo != megadottfalhasznalo or jelszo != megadottjelszo:
    if felhasznalo != megadottfalhasznalo or jelszo != megadottjelszo:
        print("Belépés megtagadtava")
        megadottfalhasznalo = input("Kérem adja meg a felhasználónevet")
        megadottjelszo = input("Kérem adja meg a jelszót")

print("Belépés engedélyezve")