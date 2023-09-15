class Szemely():
    def __init__(self, nev):
        self.nev = nev

    def info(self):
        print(f'Szia, a nevem {self.nev}', end='')

class Diak(Szemely):
    def __init__(self, nev, osztaly):
        super().__init__(nev)
        self.osztaly = osztaly

    def info(self):
        super().info()
        print(f' és a(z) {self.osztaly} osztályba járok')


class Tanar(Szemely):
    def __init__(self, nev, szak):
        super().__init__(nev)
        self.szak = szak

    def info(self):
        super().info()
        print('', '-'.join(self.szak), 'szakos tanár vagyok')



diak01 = Diak('Kiss Péter', '10.A')
tanar01 = Tanar('Horváth Zita', ['biológia', 'kémia'])
diak01.info()
tanar01.info()