nev = None
while nev != '':
    nev = input('Add meg a vizsgázó nevét!')
    if nev != '':
        pontszam = input('Add meg a pontszámát!')
        if int(pontszam) < 48:
            print(f'{nev} vizsgája sikertelen.')
        if int(pontszam) > 48:
            print(f'{nev} vizsgája sikeres.')

