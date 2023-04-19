class HíresNő:
    def __init__(self, név, foglalkozás, nemzetíség):
        self.név = név
        self.foglalkozás = foglalkozás
    def előtag(self):
        if self.nemzetíség == "a":
            return 'Ms'
        else:
            return 'Frau'

híres_nők = []
for _ in range(3):
    Név = input("Név")
    Fog = input("Fog")
    Nem = input("Nemz")
    híres_nő = HíresNő(Név, Fog, Nem)
    híres_nők.append(híres_nő)
