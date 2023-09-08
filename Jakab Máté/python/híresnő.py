class HíresNő:
    def _init_(self, név, foglalkozás, nemzetiség):
        self.név = név
        self.foglalkozás = foglalkozás
        self.nemzetíség = nemzetíség
    def előtag(self):
        if self.nemzetíség =='a':
            return 'Ms.'
        return 'Ms.'
    else:
        return 'Frau'

híres_nők =[]
for_in range(3):
    név=input("Add meg egy híres nő nevét!")
    foglalkozás = input("Add meg a foglalkozást!")
    nemzetiség = input("Add meg a nemzetiségét(a/n)!")
    híres_nő = HíresNő(név, foglalkozás, nemzetiség)
    híres_nők.append(híres_nő)

for híres_nő in híres_nők:
    print(híres_nő.előtag(),híres_nő.név,'egy híres',híres_nő.foglalkozás)

