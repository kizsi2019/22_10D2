class Diak:
    def __init__(self, nev, osztaly, szuletesi_ev):
        self.nev = nev
        self.osztaly = osztaly
        self.szuletesi_ev = szuletesi_ev
        
    def eletkor(self, aktualis_ev):
        return aktualis_ev - self.szuletesi_ev
    
    def adatok(self):
        return f"Szia, {self.nev} vagyok, a {self.osztaly} osztályba járok, {self.eletkor(2023)} éves vagyok."
