import datetime

class Diak:

    def __init__(self, nev, osztaly, szuletesiev):
        self.nev = nev
        self.osztaly = osztaly
        self.szuletesiev = szuletesiev

    def eletkor(self):
        return datetime.datetime.now().year - self.szuletesiev

    def info(self):
        print(f'Szia!', self.nev ,'vagyok! A', self.osztaly , 'osztályba járok! Életkorom', self.eletkor(),'.')

diak01 = Diak('Mikró Albert','12.A' , 2000)
diak01.info()