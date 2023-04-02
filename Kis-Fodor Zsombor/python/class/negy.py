class Negyzet:
    def __init__(self, oldalhosz):
        self.oldalhosz = oldalhosz

    def terulet(self):
        print('az terulet az:', self.oldalhosz * self.oldalhosz)

    def kerulet(self):
        print('az terulet az:', self.oldalhosz * 4)


negyzet_1 = Negyzet(6)
negyzet_1.terulet()
negyzet_1.kerulet()