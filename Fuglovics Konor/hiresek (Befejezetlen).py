class HíresNő:
    def __init__(self, nemzetiseg ,nev, foglalkozas):
        self.nemzetiseg = nemzetiseg
        self.nev = nev
        self.foglalkozas = foglalkozas

    def sentence(self):
        print(f'{self.nemzetiség} {self.név} egy híres {self.foglalkozás}.')

name = input("Add meg a híres nő nevét: ")
work = input("Add meg a foglalkozás nevét: ")
region = input("Add meg a nemzetiségét: ")

if region == "n":
