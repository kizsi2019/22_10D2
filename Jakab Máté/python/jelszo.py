nev = 'bori99'
jelszo = 'Szivecske<3'

nev2 = None
jelszo2 = None

while jelszo2 != jelszo and nev2 != nev:
    nev2 = input('Adja meg a felhasználónevét!')
    jelszo2 = input('Adja meg a jelszavát!')
    if jelszo2 != jelszo and nev2 != nev:
        print('Belépés megtagadva')

    elif jelszo2 != jelszo or nev2 != nev:
        print('Belépés megtagadva')

    else:
        print('Belépés engedélyezve')