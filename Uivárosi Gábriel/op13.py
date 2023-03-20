class Negyzet:
    def __init__(self, oldalhossz):
        self.oldalhossz = oldalhossz

    def terulet(self):
       return  self.oldalhossz * self.oldalhossz

    def kerule(self):
        return self.oldalhossz * 4
kappot = 1
lisZT = []
while kappot != 0:
   kappot = int(input("négyzet"))
   if kappot != 0:
       lisZT.append(kappot)

for szam in lisZT:

    negyzet1 = Negyzet(szam)
    print("Oldalhosza", szam)
    print("Terület" , negyzet1.terulet())
    print("Kerület",negyzet1.kerule())

