class Ember:
    def __init__(self, nev):
        self.nev = nev

    def __str__(self):
        return f"Szia, a nevem {self.nev}."


class Tanulo(Ember):
    def __init__(self, nev, osztaly):
        super().__init__(nev)
        self.osztaly = osztaly

    def __str__(self):
        return f"{super().__str__()} És a(z) {self.osztaly} osztályba járok."


class Tanar(Ember):
    def __init__(self, nev, alany):
        super().__init__(nev)
        self.alany = alany

    def __str__(self):
        return f"{super().__str__()} {self.alany} szakos tanár vagyok."


class Szulo(Ember):
    def __init__(self, nev, alany):
        super().__init__(nev)
        self.alany = alany

    def __str__(self):
        return f"{super().__str__()} {self.alany} szakos tanár vagyok."

tanulo = Tanulo("Kiss Péter", "10.A")
tanar1 = Tanar("Horváth Zita", "Biológia-kémia")
tanar2 = Tanar("Schmidt Emil", "Matematika")


print(tanulo)
print(tanar1)
print(tanar2)

with open('iskola.txt', 'w', encoding='utf-8') as celfajl:
    celfajl.write(f"Szia, a nevem {tanulo.nev}.  És a(z) {tanulo.osztaly} osztályba járok.")
    celfajl.write(tanar1.nev)
    celfajl.write(tanar2.nev)

