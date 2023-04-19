class hiresno:
    def __init__(self, nev, foglalkozas, nemzetiseg):
        self.nev = nev
        self.foglalkozas = foglalkozas
        self.nemzetiseg = nemzetiseg

    def elotag(self):
        if self.nemzetiseg == "a":
            return "Ms."
        elif self.nemzetiseg == "n":
            return "Frau"

nev = input("Add meg egy híres nő nevét! ")
foglalkozas = input("Add meg a foglalkozását! ")
nemzetiseg = input("Add meg a nemzetiségét (a/n)! ")

hiresno = hiresno(nev, foglalkozas, nemzetiseg)
print(f"{hiresno.elotag()} {hiresno.nev} egy híres {hiresno.foglalkozas}")
