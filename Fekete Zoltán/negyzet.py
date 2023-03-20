class Negyzet:
    def __init__(self, oldalhossza):
        self.oldalhossza = oldalhossza

    def terulet(self):
        return self.oldalhossza * self.oldalhossza

    def kerulet(self):
        return self.oldalhossza * 4
lista = []
hossz = input("Add meg az oldal hosszát! ")
while hossz != '0':
    negyzet = Negyzet(int(hossz))
    lista.append(negyzet)
    hossz = input("Add meg az oldal hosszát! ")
for negyzet in lista:
    print(f"A(z) {hossz} oldalhosszúságú négyzet kerülete: "
          f"{negyzet.kerulet()}, területe: {negyzet.terulet()}")
