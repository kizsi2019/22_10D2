def koszont():
    print("Üdv a fedélzeten!")

koszont()


def koszont_nevvel(nev):
    print("Szia " + nev + ", üdv a fedélzeten")

koszont_nevvel('Ádám')


def koszont_ket_nevvel(nev1, nev2):
    print('Szia ' + nev1 + ', ' + nev2 + '!\nÜdv a fedélzeten!')


koszont_ket_nevvel('Nóra', 'Ádám')


def osszead(x, y):
    eredmeny = x + y
    print("A két szám összege: ",eredmeny)

osszead(10, 9)
osszead(5+5, 5+4)

a = 10
b = 9
osszead(a, b)


def osszegzo(list):
    osszesen = 0
    for szam in list:
        osszesen = osszesen + szam
    print("A listában lévő számok összege: ",osszesen)

szamok = [3, 5, 19, 11, 17, 1]
osszegzo(szamok)


def kepernyore_irt():
    lokalis_valtozo = 'alma'
    print(lokalis_valtozo)
    print(globalis_valtozo)

globalis_valtozo = "gyümölcs"
kepernyore_irt()

print(globalis_valtozo)
