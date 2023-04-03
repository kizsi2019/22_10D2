# diák osztály
class Diak:
    # osztály adatai
    def __init__(self, név, osztály):
        self.név = név
        self.osztály = osztály

    def szoveg(self):
        print(f'Szia, a nevem {self.név}, és a(z) {self.osztály} osztályba járok.')

# tanár osztály
class Tanar:
    # osztály adatai
    def __init__(self, név, szak):
        self.név = név
        self.szak = szak

    def szoveg(self):
        print(f'Szia, a nevem {self.név}, {self.szak} szakos tanár vagyok.')

#emberek
diak1 = Diak('Kis Mihály', '10.A')
diak1.szoveg()
tanar1 = Tanar('Albert Norbert', 'Matematika')
tanar1.szoveg()