class Rect:
    def __init__(self, width):
        self.width = width

    def area(self):
        return self.width * self.width

    def kerulet(self):
        return self.width * 4


num = []
wid = input("Adj meg az oldal hosszát!")
while wid != '0':
    rectangle = Rect(int(wid))
    wid = input("Adj meg az oldal hosszát!")
    num.append(wid)
for _ in num:
    print(f"A(z) {rectangle.width} oldalhosszúságú négyzet kerülete: {rectangle.kerulet()}, területe: {rectangle.area()}")
