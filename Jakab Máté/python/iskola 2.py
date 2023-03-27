class Iskola:
    def __init__(self, lany, fiu):
        self.lany = lany
        self.fiu = fiu

    def info(self):
        print(f"Ennyi {self.lany} lány jár az iskolába és {self.fiu} fiu jár iskolába")



letszam = Iskola(200, 230)
letszam.info()

with open('iskola2.txt', 'w',  encoding= "utf-8")as forasfajl:
    forasfajl.write(f' A suliban {letszam.lany} lány jár és {letszam.fiu} fiu jár.')