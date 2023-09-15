class Kor:
    def __init__(self, sugar, kozeppont):
        self.sugar = sugar
        self.kozeppont = kozeppont

    def terulet(self):
        return self.sugar * pow(3.14, 2)

    def kerulet(self):
        return self.sugar * 3.14 * 2


kor_01 = Kor(5, (3, 7))
print(kor_01.kerulet())

kor_02 = Kor(10, (1, 1))
print(kor_02.kerulet())

