felhasznalo_nev = input("Adja meg a felhasználónevét! ")
jelszo = input("Adja meg a jelszavát! ")

while felhasznalo_nev != "bori99" or jelszo != "Szivecske<3":
    print("Belépés megtagadva.")
    felhasznalo_nev = input("Adja meg a felhasználónevét! ")
    jelszo = input("Adja meg a jelszavát! ")

print("Belépés engedélyezve.")
