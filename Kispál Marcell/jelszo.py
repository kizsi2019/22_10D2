Sajt = False

while Sajt != True:

    Felhasznalonev = input("Adja meg a felhasználónevét!")
    Jelszo = input("Adja meg a jelszavat")
    if Felhasznalonev == "bori99" and Jelszo == "szivecske<3":
        sajt = True
        print("Belépés engedélyezve")
    else:
        print("A belépés megtagadva")
