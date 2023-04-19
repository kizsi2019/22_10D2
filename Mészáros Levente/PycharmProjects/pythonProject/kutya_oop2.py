import random

nemek = ['kan', 'szuka']

class Kutya:
    def __init__(self, nev, eletkor, nem):
        self.nev = nev
        self.eletkor = random.randint(1, 10)
        self.nem = random.choice(nemek)

    def info(self):
        print(f'A kutya neve {self.nev}, a neme {self.nem}, és {self.eletkor} éves')


class Kutya1(Kutya):
    def __init__(self, nev, eletkor, nem):
        super().__init__(nev, eletkor, nem)

    def adat(self):
        super().info()


kutyak = []
while (kutya := input('add meg a kutya nevét')) != '':
    kutya_01 = Kutya1(kutya, ' ', ' ')
    kutyak.append(kutya_01)

for kutya_01 in kutyak:
    kutya_01.info()