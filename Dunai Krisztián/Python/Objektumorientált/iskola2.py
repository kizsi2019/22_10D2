class Iskola:
    def __init__(self, fiuk_szama, lanyok_szama):
        self.fiuk_szama = fiuk_szama
        self.lanyok_szama = lanyok_szama

    def kiir(self):
        with open('iskola.txt', 'w', encoding='utf-8') as cucc:
            cucc.write(f"Az iskolában {self.fiuk_szama} fiú és {self.lanyok_szama} lány tanul.")

iskola = Iskola(50, 60)

iskola.kiir()