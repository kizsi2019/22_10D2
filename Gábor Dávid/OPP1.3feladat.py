class Negyzet:
    def __init__(self, oldal_hossz):
        self.oldal_hossz = oldal_hossz

    def kerulet(self):
        return 4 * self.oldal_hossz

    def terulet(self):
        return self.oldal_hossz ** 2

lista = []
while True:
    oldal_hossz = int(input("Adjon meg egy negyzet oldalhosszat: "))
    if oldal_hossz == 0:
        break
    lista.append(Negyzet(oldal_hossz))

for negyzet in lista:
    print(f"A négyzet oldalhossza: {negyzet.oldal_hossz}")
    print(f"A négyzet kerülete: {negyzet.kerulet()}")
    print(f"A négyzet területe: {negyzet.terulet()}")
