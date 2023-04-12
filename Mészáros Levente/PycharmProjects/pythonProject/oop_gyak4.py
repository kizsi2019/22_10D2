class Diak:
    def __init__(self, nev, osztaly, szuletesi_ev):
        self.nev = nev
        self.osztaly = osztaly
        self.szuletesi_ev = szuletesi_ev

    def info(self):
        print(f'Szia, nevem {self.nev}, és a {self.osztaly} osztályba járok, {2023 - int(self.szuletesi_ev)} éves vagyok')


diak_01 = Diak('Kiss Péter', '10.A', '2007')
diak_01.info()