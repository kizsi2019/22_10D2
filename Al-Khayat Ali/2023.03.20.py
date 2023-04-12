class Szemely():
    def __init__(self, nev):
        self.nev = nev

    def bemutatkozas(self):
        print(f'szia a nevem {self.nev}', end='')

class Diak (Szemely):
    def __init__(self, nev, osztaly):
        super().__init__(nev)
        self.osztaly = osztaly

    def bemutatkozas(self):
        super().bemutatkozas()
        print(f' és a {self.osztaly} osztalyba jarok.')

class Tanar(Szemely):
    def __init__(self, nev, szakok):
        super().__init__(nev)
        self.szakok = szakok
    def bemutatkozas(self):
        super().bemutatkozas()
        print('', '-'.join(self.szakok), 'szakos tanár vagyok')

diak01 = Diak('Kiss Péter', '10.A')
tanar01 = Tanar('Horváth Zita', ['biológia','kémia'])
tanar02 = Tanar('Schmidt Emil', ['matematika'])
diak01.bemutatkozas()
tanar01.bemutatkozas()
tanar02.bemutatkozas()