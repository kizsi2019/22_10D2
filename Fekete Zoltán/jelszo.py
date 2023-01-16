ertek = True
while ertek == True:
    nevadas = input("Adja meg a felhasználónevét!")
    jelszoadas = input("Adja meg a jelszavát!")
    if jelszoadas == "Szivecske<3" and nevadas == "bori99":
        print("Belépés engedélyezve.")
        ertek = False
    else:
        print("Belépés megtagadva.")
