class Negyzet:
    def __init__(self, oldalhossz):
        self.oldalhossz = oldalhossz

    def terulet(self):
        return self.oldalhossz * self.oldalhossz

    def kerulet(self):
       return self.oldalhossz * 4

lista = []
hossz = (input("Add meg az oldal hosszát!"))
while hossz != '0':
        negyzet = Negyzet(int(hossz))
        lista.append(negyzet)
        hossz = input("Add meg az oldal hosszát!")

for negyzet in lista:
    print(f"A(z) {negyzet.oldalhossz} oldalhosszúságú négyzet kerülete: {negyzet.kerulet()}, területe: {negyzet.terulet()}")