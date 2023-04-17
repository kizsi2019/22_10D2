class Szemely():
    def __init__(self, nev):
        self.nev = nev

    def info(self):
        print(f'Szia, a nevem {self.nev},', end='')


class Gyerek1(Szemely):
    def __init__(self, nev, eletkor, nem):
        super().__init__(nev)
        self.eletkor = eletkor
        self.nem = nem

    def bemutatkozas(self):
        super().info()
        print(f' {self.eletkor} éves vagyok, és {self.nem}')


class Gyerek2(Szemely):
    def __init__(self, nev, eletkor, nem):
        super().__init__(nev)
        self.eletkor = eletkor
        self.nem = nem

    def bemutatkozas(self):
        super().info()
        print(f' {self.eletkor} éves vagyok, és {self.nem}')


Flora = Gyerek1('Flóra', 11, 'lány')
Flora.bemutatkozas()

Laca = Gyerek2('Laci', 7, 'fiú')
Laca.bemutatkozas()
