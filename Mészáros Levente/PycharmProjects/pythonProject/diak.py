import datetime

class Diak:


    def __init__(self, nev, osztaly, szuletesi_ev):
        self.nev = nev
        self.osztaly = osztaly
        self.szuletesi_ev = szuletesi_ev

    def eletkor(self):
        aktualis_ev = 2023
        return aktualis_ev - self.szuletesi_ev

    def adatok(self):
        print(f"Szia, {self.nev} vagyok, a {self.osztaly} osztályba járok, {self.eletkor()} éves vagyok")


diak_1 = Diak('Kiss Péter', '10A', 2007)
diak_1.adatok()



