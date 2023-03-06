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