
class Negyzet:
    def __init__(self, oldalhossz):
        self.oldalhossz = oldalhossz

    def terulet(self):
        print("A nyégzet területe", self.oldalhossz * self.oldalhossz)

    def kerule(self):
        print("A négyzet kerülete: ", self.oldalhossz * 4 )

negyzet_1 =Negyzet(6)
negyzet_1.terulet()
negyzet_1.kerule()

