class HíresNő:
    def __init__(self, nemzetiseg ,nev, foglalkozas):
        self.nemzetiseg = nemzetiseg
        self.nev = nev
        self.foglalkozas = foglalkozas

    def start(self):
        if self.nemzetiseg == "n":
            return "Frau"
        else:
            return "Ms."

women = []
for i in range(3):
    name = input("Add meg a híres nő nevét: ")
    work = input("Add meg a foglalkozás nevét: ")
    region = input("Add meg a nemzetiségét: ")
    woman = HíresNő()
    women.append(woman)

for woman in women:
    print(f"{HíresNő.start} {woman.nev} egy híres {woman.foglalkozas}.")