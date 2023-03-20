korok = []
for _ in range(5):
    kor = Kor(random.randint(0, 10))
    korok.append(kor)

for kor in korok:
    kor.info()
    korok[0].info()
  

class Negyzet:
    def __init__(self, oldalhossz):
        self.oldalhossz = oldalhossz
    def terulet(self):
        return self.oldalhossz ∗ self.oldalhossz

    def kerulet(self):
        return self.oldalhossz × 4


negyzet_1 =Negyzet(6)
negyzet_1.terulet()
negyzet_1.kerulet()