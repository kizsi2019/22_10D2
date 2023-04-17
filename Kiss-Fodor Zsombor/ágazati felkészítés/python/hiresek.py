class HíresNő:
    def __init__(self, név, foglalkozás, ország):
        self.név = név
        self.foglalkozás = foglalkozás
        self.ország = ország

    def előtag(self):
        if self.ország == "a":
            print(f"Ms. {self.név} egy híres {self.foglalkozás}")
        else:
            print(f"Frau {self.név} egy híres {self.foglalkozás}")

no1nev = input("Add meg egy híres nő nevét!")
no1munka = input("Add meg a foglalkozását!")
no1orszag = input("Add meg a nemzetiségét (a/n)!")
no1 = HíresNő(no1nev, no1munka, no1orszag)

no2nev = input("Add meg egy híres nő nevét!")
no2munka = input("Add meg a foglalkozását!")
no2orszag = input("Add meg a nemzetiségét (a/n)!")
no2 = HíresNő(no2nev, no2munka, no2orszag)

no3nev = input("Add meg egy híres nő nevét!")
no3munka = input("Add meg a foglalkozását!")
no3orszag = input("Add meg a nemzetiségét (a/n)!")
no3 = HíresNő(no3nev, no3munka, no3orszag)

no1.előtag()
no2.előtag()
no3.előtag()