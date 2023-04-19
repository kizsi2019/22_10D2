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

híres_nők = []
for _ in range(3):
    nev = input("Add meg egy híres nő nevét! ")
    foglalkozas = input("Add meg a foglalkozását! ")
    nemzetiseg = input("Add meg a nemzetiségét (a/n)! ")
    híres_nő = hiresno(nev,foglalkozas,nemzetiseg)
    híres_nők.append(híres_nő)

for híres_nő in híres_nők:
    print(híres_nő.elotag(), híres_nő.nev,'egy híres', híres_nő.foglalkozas)
