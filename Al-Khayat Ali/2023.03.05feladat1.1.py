class Negyzet:
        def __int__(self, oldalhossz):
            self.oldalhossz = oldalhossz
        def terulet(self):
            print("A négyzet területe: ", self.oldalhossz * self.oldalhossz)
        def kerulet(self):
            print("A négyzet területe: ", self.oldalhossz * 4)

negyzet_1 =Negyzet(6)
negyzet_1.terulet()
negyzet_1.kerulet()