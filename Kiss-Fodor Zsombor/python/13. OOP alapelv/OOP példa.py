import datetime

# gépjármű osztály
class Gepjarmu:
    # megadjuk az objektumot, és adatait
    def __init__(self, rendszam, ossz_km, kov_szerviz, szakasz_km):
        self.rendszam = rendszam
        self.ossz_km = ossz_km
        self.kov_szerviz = kov_szerviz
        self.szakasz_km = szakasz_km

    def szerviz(self):
        return self.kov_szerviz - datetime.datetime.now().year

    def vissza_km(self):
        return 'Benzines vagy elektromos?'


class Taxi(Gepjarmu):
    def __init__(self, rendszam, ossz_km, kov_szerviz, szakasz_km, fogyasztas=6.0, tank_l=35):
        super().__init__(rendszam, ossz_km, kov_szerviz, szakasz_km)
        self.fogyasztas = fogyasztas
        self.tank_l = tank_l

    def vissza_km(self):
        return round(self.tank_l / self.fogyasztas * 100 - self.szakasz_km)


class ETaxi(Gepjarmu):
    def __init__(self, rendszam, ossz_km, kov_szerviz, szakasz_km, hatotav=600):
        super().__init__(rendszam, ossz_km, kov_szerviz, szakasz_km)
        self.hatotav = hatotav

    def vissza_km(self):
        return self.hatotav - self.szakasz_km

# egy objektumunk
Suzuki_Ignis = Gepjarmu('IZG185', 280000, 2025,100)