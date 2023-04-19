engedely = False

while not engedely:
    nev = input("Adja meg a felhasználónevét!")
    jelszo = input("Adja meg a jelszavát!")
    helyesnev = "bori99"
    helyesjelszo = "Szivecske<3"

    if nev == helyesnev and jelszo == helyesjelszo:
        print("Belépés engedélyezve.")
        engedely = True
    else:
        print("Belépés megtagadva.")
