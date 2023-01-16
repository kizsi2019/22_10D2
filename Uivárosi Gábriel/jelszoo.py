T = False
while T == False :
   fehasznalo = input("Adja meg a felhasználónevét!")
   jelszo = input("Adja meg a jelszavát!")
   if fehasznalo == "bori99" and jelszo == "Szivecske<3":
       T = True
       print("Belépés engedélyezve. ")
   else:
       print("Belépés megtagadva.")