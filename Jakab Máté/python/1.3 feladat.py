class Negyzet:
    def __init__(self, oldal_hossz):
        self.oldal_hossz = oldal_hossz

    def kerulet(self):
        print(4 * self.oldal_hossz)

    def terulet(self):
        print(self.oldal_hossz ** 2)

    def kerulet(self):
        print("A négyzet kerülete: ", self.oldal_hossz *4)

negyzet_1 =Negyzet(12)
negyzet_1.terulet()
negyzet_1.kerulet()

class Negyzet:
    def __init__(self, oldal_hossz):
        self.oldal_hossz = oldal_hossz

    def kerulet(self):
        return 4 * self.oldal_hossz

    def terulet(self):
        return self.oldal_hossz ** 2


# Lista inicializálása
negyzetek = []

while True:
    oldal_hossz = float(input("Kérem adja meg a négyzet oldalhosszát (0 ha vége): "))
    if oldal_hossz == 0:
        break
    negyzet = Negyzet(oldal_hossz)
    negyzetek.append(negyzet)

print("A megadott négyzetek oldalhossza, kerülete és területe:")

for negyzet in negyzetek:
    print("Oldalhossz: {} | Kerület: {} | Terület: {}".format(
        negyzet.oldal_hossz, negyzet.kerulet(), negyzet.terulet()))