class HíresNő:
    def __init__(self, név, foglalkozás, orszag):
        self.név = név
        self.foglalkozás = foglalkozás
        self.orszag = orszag

    def info(self):
        if self.orszag == "a":
            print(f"Ms. {self.név} egy híres {self.foglalkozás}")
        else:
            print(f"Frau {self.név} egy híres {self.foglalkozás}")

no1nev=input("Add meg egy híres nő nevét!")
no1foglalkozas=input("Add meg a foglalkozását!")
no1orszag=input("Add meg a nemzetiségét (a/n)")

no2nev=input("Add meg egy híres nő nevét!")
no2foglalkozas=input("Add meg a foglalkozását!")
no2orszag=input("Add meg a nemzetiségét (a/n)")

no3nev=input("Add meg egy híres nő nevét!")
no3foglalkozas=input("Add meg a foglalkozását!")
no3orszag=input("Add meg a nemzetiségét (a/n)")

no1=HíresNő(no1nev,no1foglalkozas,no1orszag)
no2=HíresNő(no2nev,no2foglalkozas,no2orszag)
no3=HíresNő(no3nev,no3foglalkozas,no3orszag)

no1.info()
no2.info()
no3.info()