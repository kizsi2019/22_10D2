import random

vezeteknev = ['Kiss', 'Balogh', 'Mészáros', 'Halmos', 'Demmel', 'Nagy', 'Iszály', 'Vicsápi', 'Dunai', 'Elekes']
keresztnev = ['Réka', 'Péter', 'Levente', 'Károly', 'Csilla', 'Márk', 'Barnabás', 'Bence', 'Andrea', 'László']


class Iskola:
    def __init__(self, nev, osztaly, szuletesi_ev):
        self.nev = nev
        self.osztaly = random.randint(9, 13)
        self.szuletesi_ev = random.randint(2004, 2006)

    def info(self):
        print(f'Szia, a nevem {self.nev}, a {self.osztaly}. osztályba járok, és {self.szuletesi_ev} ban/ben születtem')


class Diak(Iskola):
    def __init__(self, nev, osztaly, szuletesi_ev):
        super().__init__(nev, osztaly, szuletesi_ev)

    def adat(self):
        super().info()


Diakok = []
for _ in range(5):
    vezeteknev2 = random.choice(vezeteknev)
    keresztnev2 = random.choice(keresztnev)
    diak_01 = Diak(vezeteknev2 + ' ' + keresztnev2, ' ', ' ')
    Diakok.append(diak_01)

for diak_01 in Diakok:
    diak_01.info()