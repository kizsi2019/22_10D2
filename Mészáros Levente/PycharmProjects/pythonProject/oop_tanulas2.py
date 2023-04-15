import random

class Kor:
    def __init__(self, sugar, kozeppont=(0, 0)):
        self.sugar = sugar
        self.kozeppont = kozeppont

    def terulet(self):
        return self.sugar * pow(3.14, 2)

    def kerulet(self):
        return self.sugar * 3.14 * 2

korok = []
for _ in range(5):
    kor = Kor(random.randint(1, 10))
    korok.append(kor)

for kor in korok:
    print(kor.sugar, kor.kerulet())

print(korok[1].sugar)