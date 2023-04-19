import math

class Negyzet:
    def __init__(self, oldalhossz):
        self.oldalhossz = oldalhossz

    def info(self):
        print(f'Egy {self.oldalhossz} cm hosszúságú négyzet területe {math.pow(self.oldalhossz, 2):.0f} cm², kerülete pedig {self.oldalhossz *4 } cm')

negyzetek = []
while (negyzet := int(input('Add meg a négyzet oldalhosszát!'))) > 0:
    negyzet_01 = Negyzet(negyzet)
    negyzetek.append(negyzet_01)

for negyzet_01 in negyzetek:
    negyzet_01.info()