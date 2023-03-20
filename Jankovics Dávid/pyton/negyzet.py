class Negyzet:
    def __init__(self, oldal_hossz):
        self.oldal_hossz = oldal_hossz
    
    def kerulet(self):
        return 4 * self.oldal_hossz
    
    def terulet(self):
        return self.oldal_hossz ** 2


negyzetek = []  
oldal_hossz = int(input("Adjon meg egy négyzet oldalhosszát (vagy 0-át a kilépéshez): "))
while oldal_hossz != 0:
    negyzet = Negyzet(oldal_hossz)  
    negyzetek.append(negyzet)  
    oldal_hossz = int(input("Adjon meg egy négyzet oldalhosszát (vagy 0-át a kilépéshez): "))



for negyzet in negyzetek(negyzetek):
    print(f"A{z} négyzet:")
    print(f"\toldalhossz: {negyzet.oldal_hossz}")
    print(f"\tkerület: {negyzet.kerulet()}")
    print(f"\tterület: {negyzet.terulet()}")
