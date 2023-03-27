class Ember:
    def __init__(self, nev):
        self.nev = nev

class Diak(Ember):
    def __init__(self, nev, osztaly):
        super().__init__(nev)
        self.osztaly = osztaly
    
    def bemutatkozas(self):
        return f"Szia, a nevem {self.nev}, és a(z) {self.osztaly} osztályba járok."

class Tanar(Ember):
    def __init__(self, nev, szak):
        super().__init__(nev)
        self.szak = szak
    
    def bemutatkozas(self):
        return f"Szia, a nevem {self.nev}, {self.szak} szakos tanár vagyok."



diak1 = Diak("Kiss Péter", "10.A")
tanar1 = Tanar("Horváth Zita", "biológia-kémia")
tanar2 = Tanar("Schmidt Emil", "matematika")
