import random

nemek = ['kan', 'szuka']

class Kutya():
    def __init__(self, nev):
        self.nev = nev

    def info(self):
        print(f'A kutya neve {self.nev},', end='')


class Kutya1(Kutya):
    def __init__(self, nev, eletkor, nem):
        super().__init__(nev)
        self.eletkor = random.randint(1, 10)
        self. nem = random.choice(nemek)

    def info(self):
        super().info()
        print(f' a neme {self.nem}, és {self.eletkor} éves')



kutyak = []
while (kutya := input('Add meg a kutya nevét!')) != '':
    kutya01 = Kutya1(kutya, ' ', ' ')
    kutyak.append(kutya01)

for kutya01 in kutyak:
    kutya01.info()