class Negyzet:
    def __init__(self, oldal_hossz):
        self.oldal_hossz = oldal_hossz

    def kerulet(self):
        return 4 * self.oldal_hossz

    def terulet(self):
        return self.oldal_hossz ** 2

negyzetek = []

while True:
    oldal_hossz = float(input("Kérem a négyzet oldalhosszát (0 kilépéshez): "))
    if oldal_hossz == 0:
        break
    negyzet = Negyzet(oldal_hossz)
    negyzetek.append(negyzet)

print("A megadott négyzetek adatai:")
for i, negyzet in enumerate(negyzetek):
    print(f"{i + 1}. négyzet oldalhossza: {negyzet.oldal_hossz:.2f}")
    print(f"{i + 1}. négyzet kerülete: {negyzet.kerulet():.2f}")
    print(f"{i + 1}. négyzet területe: {negyzet.terulet():.2f}")
