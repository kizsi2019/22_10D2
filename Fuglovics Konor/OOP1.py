import random
class Circle:
    def __init__(self, sugar, center=(0, 0)):
        self.center = center
        self.sugar = sugar

    def area(self):
        return self.sugar * pow(3.14, 2)

    def kerulet(self):
        return self.sugar * 2 * 3.14

    def info(self):
        print(f'A(z) {self.sugar} egység sugarú, {self.center} középpontú kör területe {self.area():.2f} egység, kerülete {self.kerulet():.2f} egység')

circle_01 = Circle(5, (2, 6))

print(circle_01)
print(type(circle_01))
print(isinstance(circle_01, Circle))

print(circle_01.area())

circles = []
for _ in range(5):
    circle = Circle(random.randint(0, 10))
    circles.append(circle)

for circle in circles:
    circle.info()

circles[0].info()