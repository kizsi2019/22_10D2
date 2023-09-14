felhasznalo_nev = 'bori99'
jelszo = 'Szivecske<3'


szo = ''
szo2 = ''

sikertelen = 0
sikeres = 0

while szo != felhasznalo_nev or szo2 != jelszo:
    szo = input('Adja meg a felhasználó nevét!')
    szo2 = input('Adja meg a jelszavát!')
    if szo != felhasznalo_nev or szo2 != jelszo:
        print('belépés megtagadva')
        sikertelen += 1


if szo == felhasznalo_nev and szo2 == jelszo:
    print('belépés engedélyezve')
    sikeres += 1


print('sikertelen jelszókísérlet', sikertelen)
print('sikeres jelszókísérlet', sikeres)














