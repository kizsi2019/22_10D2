class kor:
    def __init__(self, sugar, kozeppont=(0,0)):
        self.kozeppont = kozeppont
        self.sugar = sugar

    def terulet(self):
        return self.sugar * pow(3.14, 2)

    def kerulet(self):
        return self.sugar * 2 * 3.14

    def info(self):
        print(f'A(z) {self.sugar} egység sugaru  ')