import random

vezeteknev = ['Kiss', 'Balogh', 'Mészáros', 'Halmos', 'Demmel']
keresztnev = ['Réka', 'Péter', 'Levente', 'Károly', 'Csilla']

vezeteknev2 = random.choice(vezeteknev,)
keresztnev2 = random.choice(keresztnev)

class Iskola():
    def __init__(self, vezeteknev, keresztnev, osztaly, szuletesi_ev):
        self.vezeteknev = vezeteknev2
        self.keresztnev = keresztnev2
        self.osztaly = random.randint(10, 13)
        self.szuletesi_ev = random.randint(2004, 2006)

    def info(self):
        print(f'Szia, a nevem {self.vezeteknev  + self.keresztnev}, a {self.osztaly}. osztályba járok, és {self.szuletesi_ev} ban/ben születtem')

class Diak(Iskola):
    def __init__(self, vezeteknev, keresztnev, osztaly, szuletesi_ev):
        super().__init__(vezeteknev, keresztnev, osztaly, szuletesi_ev)

    def adatok(self):
        super().info()

Diakok = []
for _ in range(5):
    diak_01 = Diak(' ', ' ', ' ', ' ')
    Diakok.append(diak_01)

for diak_01 in Diakok:
    diak_01.adatok()