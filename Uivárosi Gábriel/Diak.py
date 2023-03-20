import datetime


class Diak:

    def __init__(self, nev ,osztaly , szul_ev):
        self.nev = nev
        self.osztaly = osztaly
        self.szul_nev = szul_ev

    def Nevem(self):
        return "Az én nevem", self.nev

    def osztalyom(self):
        return "Az osztály amibe játok", self.osztaly


    def evszamok(self):
        return "Én", datetime.datetime.now().year - self.szul_nev ,"éves vagyok"

    def mondat(self):
        return "szia én", self.nev , "vagyok és a " , self.osztaly , "ba/be járok, és  ", datetime.datetime.now().year - self.szul_nev ,"éves vagyok"

Diak_1 = Diak('KÁLVIN', '3G' , 2005)
print(Diak.Nevem(Diak_1))
print(Diak.osztalyom(Diak_1))
print(Diak.evszamok(Diak_1))
print(Diak.mondat(Diak_1))

