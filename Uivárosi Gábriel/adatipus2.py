'''
def tarolo():
    sor = ["0 0 0"]
    kocka = [sor, sor , sor]
    for elem in kocka:
        print(elem)


tarolo()
'''
def tarolo():
   sor = int(input("sor"))
   oszlop = int(input("oszlop"))
   tarolof = []
   sorszam = 0
   oszlopszam = 0

   for o in range(3):
       egy_sor = []
       sorszam = sorszam + 1
       oszlopszam = 0
       for z in range(3):
          oszlopszam = oszlopszam + 1
          if sor == sorszam and oszlop == oszlopszam:
             egy_sor.append("+")
          else:
             egy_sor.append("0")
       tarolof.append(egy_sor)
   for t in tarolof:
      print(t)
tarolo()

