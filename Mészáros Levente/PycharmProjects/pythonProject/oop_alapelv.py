class Diak:
    def __init__(self, nev, osztaly):
        self.nev = nev
        self.osztaly = osztaly

    def info(self):
        print(f"Szia, {self.nev} vagyok, a {self.osztaly} osztályba járok")

diak_1 = Diak('Kiss Péter', '10.A')
diak_1.info()


class Tanar:
    def __init__(self, nev, szak):
        self.nev = nev
        self.szak = szak


    def info(self):
        print(f"Szia, {self.nev} vagyok, és {self.szak} szakos tanár vagyok")

tanar_1 = Tanar('Horváth Zita', ' biológia-kémia')
tanar_1.info()
tanar_2 = Tanar('Schmidt Emil', 'matematika')
tanar_2.info()



with open('iskola.txt', 'w', encoding='utf_8') as celfajl:
    celfajl.write(f"Szia, {tanar_1.nev} vagyok, és {tanar_1.szak} szakos tanár vagyok\n")
    celfajl.write(f"Szia, {diak_1.nev} vagyok, és {diak_1.osztaly} szakos tanár vagyok")