

class Szemely():
    def __init__(self, nev):
        self.nev = nev

    def bemutatkozas(self):
        print(f'Szia, a nevem {self.nev}', end='')

class Diak(Szemely):
    def __init__(self, nev, osztaly):
        super().__init__(nev)
        self.osztaly = osztaly

    def bemutatkozas(self):
        super().bemutatkozas()
        print(f' és a(z) {self.osztaly} ba járok.')


class Tanar(Szemely):
    def __init__(self, nev, szakok):
        super().__init__(nev)
        self.szakok = szakok

    def bemutatkozas(self):
        super().bemutatkozas()
        print('','-'.join(self.szakok), 'szakos tanár vagyok.')

diak01 = Diak('Kiss Péter', '10A')
tanar01 = Tanar('Bekre Pál',  ['biológia', 'matematika'])
tanar02 = Tanar('Bármi Áron',  ['Történelem'])

tanar02.bemutatkozas()
diak01.bemutatkozas()
tanar01.bemutatkozas()