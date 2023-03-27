class Diak:

    def __init__(self, nev, osztaly, szuletesi_ev):
        self.nev = nev
        self.osztaly = osztaly
        self.szuletesi_ev = szuletesi_ev

    def eletkor(self):
            aktualis_ev = 2023
            return aktualis_ev - self.szuletesi_ev

    def info(self):
        print("szia (self.nev) vagyok (self.szuletesi_ev) be születtem és a (self.osztaly) be járok")

diak_1 = Diak('Kiss Péter' ,'10A','16')
diak_1.adatok()

class Tanar:

    def __init__(self, nev, szak):
        self.nev = nev
        self.szak = szak

    def info(self):
        print("szia (self.nev) vagyok (self.szak) tanár vagyok")

tanar_1 = Tanar('Horváth Zita', 'Biológia_Kémia')
tanar_2 = Tanar('Schmidt Emil', 'Matematika')



