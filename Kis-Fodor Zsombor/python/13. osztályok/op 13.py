class Negyzet:
    def __init__(self, oldalhosz):
        self.oldalhosz = oldalhosz

    def terulet(self):
        return self.oldalhosz * self.oldalhosz

    def kerulet(self):
        return self.oldalhosz * 4

Negyzetek = []

Inputu = input('adj egy számot')

while Inputu != '0':
    negyzet = Negyzet(int(Inputu))
    Negyzetek.append(negyzet)
    Inputu = input('adj egy számot')

for negyzet in Negyzetek:
    print(F"a(z), {negyzet.oldalhosz},hosszusago negyzet terulete az:, {negyzet.terulet()},a kerulete:, {negyzet.kerulet()}")