import datetime

class Diak:

    def __init__(self, nev, osztaly, szuletesi_ev):
        self.nev = nev
        self.osztaly = osztaly
        self.szuletesi_ev = szuletesi_ev

    def eletkor(self):
        aktualis_ev = 2023  # vagy barmilyen mas ev, amelyben az eletkor szamitasat szeretned vegrehajtani
        return aktualis_ev - self.szuletesi_ev

    def adatok(self):
        return f"Szia, {self.nev} vagyok, a {self.osztaly} osztályba járok, {self.eletkor()} éves vagyok."

diak1 = Diak("Kiss Péter", "10.A", 2007)
print(diak1.diak_info(2023))
"Szia, Kiss Péter vagyok, a 10.A osztályba járok, 16 éves vagyok."
