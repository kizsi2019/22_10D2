class Negyzet:
    def __init__(self, oldalhossz):
        self.oldalhossz = oldalhossz

    def terulet(self):
        print(f"a négyzet területe: {4 * self.oldalhossz}")

    def kerulet(self):
        print(f"a négyzet kerülete: {2 * self.oldalhossz}")

negyzet_1 = Negyzet(12)
negyzet_1.terulet()
negyzet_1.kerulet()