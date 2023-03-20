import datetime


class Diak:

    def __init__(self, nev, osztaly, szuletesiev,):
        self.nev = nev
        self.osztaly = osztaly
        self.szuletesiev = szuletesiev

    def eletkor(self):
        return datetime.datetime.now().year - self.szuletesiev

    def info(self):
        print(f"Szia, {self.nev} vagyok a {self.osztaly} osztályba járok, {self.eletkor()} éves vagyok")

diak_1 = Diak('Kiss Péter', '10.A', 2007)
diak_1.info()