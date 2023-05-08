bejutott = False

while not bejutott:
    felhasznalonev = input("Adja meg a felhasználónevét! ")
    jelszo = input("Adja meg a jelszavát! ")

    if felhasznalonev == 'bori99' and jelszo == 'Szivecske<3':
        print("A belépés engedélyezve.")
        bejutott = True
    else:
        print("A belépés megtagadva.")