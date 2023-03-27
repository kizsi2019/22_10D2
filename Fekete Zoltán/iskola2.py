class Iskola:
    def __init__(self, fiuk, lanyok):
        self.fiuk = fiuk
        self.lanyok = lanyok

    def __str__(self):
        return f"Az iskolába {self.fiuk} fiú jár, és {self.lanyok} lány jár."

letszam_02 = Iskola("100", "200")
print(letszam_02)

letszam_01 = Iskola(100, 200)

with open('iskola2.txt', 'w', encoding='utf-8') as celfajl:
    celfajl.write(f'Az iskolába {letszam_01.fiuk} fiú, és {letszam_01.lanyok} lány jár.')