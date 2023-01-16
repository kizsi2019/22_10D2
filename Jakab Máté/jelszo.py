Felhasznalonev = 'bori99'
jelszo = 'Szivecske<3'

szo = ''
szo2 = ''

sikeres = 0
sikertelen = 0

while szo != Felhasznalonev or szo2 != jelszo:
    szo = input('Add meg a felhasználónevet ')
    szo2 = input('Add meg a jelszót ')
    if szo != Felhasznalonev or szo2 !=jelszo:
        print('belépés sikertelen')
        sikertelen +=1

    if szo == Felhasznalonev or szo2 == jelszo:
        print('belépés jóváhagyva')
        sikeres += 1

print('sikertelen jelszó kísérlet',sikertelen )
print('sikeres jelszó kisérlet',sikeres )