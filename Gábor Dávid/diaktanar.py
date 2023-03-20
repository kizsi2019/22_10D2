class Szemely():
    def __init__(self, nev):
        self.nev = nev

class Diak(Szemely):

    def __init__(self, nev, osztaly, ):
        super().__init__(nev)
        self.osztaly = osztaly

    def info(self):
        print(f"Szia, {self.nev} vagyok a {self.osztaly} osztályba járok")

class Tanar(Szemely):
    def __init__(self, nev, szak,):
        super().__init__(nev)
        self.szak = szak

    def info(self):
        print(f"Szia, {self.nev} vagyok és {self.szak} tanár vagyok.")

diak_1 = Diak('Kiss Péter', '10.A')
diak_1.info()
tanar_1 = Tanar('Horváth Zita', 'Matematika')
tanar_1.info()