def sikeres_e(pontszam):
    return pontszam >= 48

def vizsga():
    while True:
        nev = input('Add meg a nevedet!')
        if nev == '':
            break
        pontszam_str = input('Add meg a pontszámát!')
        pontszam = int(pontszam_str)

        if sikeres_e(pontszam):
            print('A vizsgázó át jutott')

vizsga()