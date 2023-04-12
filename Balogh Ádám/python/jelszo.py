felhasznalo = "bori99"
jelszo = "Szivecske<3"

jfelhasznalo = input("Adja meg a felhasználó nevet!")
jjelszo = input("Adja meg a jelszót!")

while felhasznalo != jfelhasznalo or jelszo != jjelszo:
    if felhasznalo != jfelhasznalo or jelszo != jjelszo:
        print("Belépés megtagadva!")
        jfelhasznalo = input("Adja meg a felhasználó nevet!")
        jjelszo = input("Adja meg a jelszót!")

print("Belépés engedélyezve.")