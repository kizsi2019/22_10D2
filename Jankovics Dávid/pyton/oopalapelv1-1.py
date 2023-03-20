
class szemely():
    def __init__(self, nev):
            self.nev = nev

    def bemutatkozik(self):
          print(f"Szia, a nevem {self.nev}", end='')



class Diak(szemely):


    def __init__(self, nev, osztaly):
            self.nev = nev
            self.osztaly = osztaly

    def bemutatkozik(self):
        super().bemutatkozik()
        print(f", és a {self.osztaly} osztályba járok ")
    


class Tanár(szemely):
        def __init__(self, nev, szakok):
            super().__init__(nev)
            self.szakok = szakok


diak01 = Diak('Jankovics Dávid', '10.D')
tanár01 = Tanár('Jancsi', ['matek', 'fizika'])
tanár02 = Tanár('józsi', ['angol', 'magyar'])

print(diak01.nev, diak01.osztaly)
diak01.bemutatkozik()