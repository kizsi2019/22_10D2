felhasznalonev = "bori99"
jelszo = "Szivecske<3"

nev = input("Add meg a felhasználóneved!")
jel = input("Add meg a jelszavad!")

if nev == felhasznalonev:
    print("")

if jel == jelszo and nev == felhasznalonev:
    print("Sikeres bejelentkezés!")

if nev != felhasznalonev:
    print("Hibás felhasználónev!")

if jel != jelszo:
    print("Hibás jelszó!")