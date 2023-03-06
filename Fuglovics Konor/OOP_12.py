class Rect:
    def __init__(self, width):
        self.width = width

    def area(self):
        print("A négyzet területe:", self.width * 2)

    def district(self):
        print("A négyzet kerülete:", self.width * 4)


rect1 = Rect(6)
rect1.area()
rect1.district()
