import math

class Negyzet:
    def __init__(self, oldalhossz):
        self.oldalhossz = oldalhossz

    def terulet(self):
        print(f'A négyzet területe {math.pow(self.oldalhossz, 2)} cm²')

    def kerulet(self):
        print(f'A négyzet kerülete {self.oldalhossz * 4} cm')



negyzetek = []
while (szam := int(input('Add meg a négyzet oldalhosszát!'))) > 0:
    negyzet_01 = Negyzet(szam)
    negyzetek.append(negyzet_01)

for negyzet in negyzetek:
    negyzet_01.terulet()
    negyzet_01.kerulet()


