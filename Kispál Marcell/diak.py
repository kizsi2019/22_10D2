class Diak:


    def __init__(self,nev,osztaly,szuletesi_ev):
        self.nev = nev
        self.osztaly = osztaly
        self.szuletesi_ev

    def eletkor(self):
        aktualis_ev = 2023
        return aktualis_ev - self.szuletesi_ev

    def info(self):
        print(f"szia {self.nev} vagyok, a{self.osztaly} osztályba járok, {self,életkor} éves vagyok")

diak_1 = Diak('Kiss Péter', '10A', 2007)
diak_1.adatok()