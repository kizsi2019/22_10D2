class Tanar:
    def __init__(self, nev, szak):
        super().__init__(nev)
        self.szak = szak
    
    def bemutatkozas(self):
        return f"Szia, a nevem {self.nev}, {self.szak} szakos tanár vagyok."

diak_01.info()
tanar_01.info()
tanar_02.info()
print(tanar_01.nev)
print(diak_01.osztaly)

with open('iskola.txt', 'w', encoding='utf-8') as celfajl:
        celfajl.write(diak_01.nev)
        celfajl.write(tanar_01.nev)
        celfajl.write(tanar_02.nev)
