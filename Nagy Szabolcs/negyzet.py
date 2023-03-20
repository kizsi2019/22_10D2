class Negyzet:
    def __init__(self, oldalhossz):
        self.oldalhossz = oldalhossz

    def terulet(self):
        print("A négyzet területe:",  self.oldalhossz * self.oldalhossz)

    def kerulet(self):
        print("A négyzet kerülete:",  self.oldalhossz * 4)

negyzet_1 =Negyzet(12)
negyzet_1.terulet()
negyzet_1.kerulet()