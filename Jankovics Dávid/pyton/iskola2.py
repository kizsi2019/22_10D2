

class Iskola:
    def __init__(self, fiu, lany):
            self.fiu = fiu
            self.lany = lany

            
iskola01 =Iskola(100,200)

with open('iskola2.txt', 'w', encoding='utf-8') as celfajl:
      celfajl.write(f'az iskolába {iskola01.fiu} fiu, és {iskola01.lany} lány jár')
