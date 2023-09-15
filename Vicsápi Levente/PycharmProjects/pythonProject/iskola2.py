class Iskola:
    def __init__(self, fiuk, lanyok):
        self.lanyok = lanyok
        self.fiuk = fiuk

    def info(self):
        print(f"A suliban {self.fiuk} van és {self.lanyok} lány van.")

letszam = Iskola(100, 150)
letszam.info()

with open('iskola2.txt', 'w', encoding='utf-8') as celfajl:
    celfajl.write(f"A suliban {letszam.fiuk} fiú van és {letszam.lanyok} lány van.")