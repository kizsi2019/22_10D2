'''
Az adatok beolvasása fájlból,
egy-egy sor az 'adatok' nevű lista egy-egy eleme
'''
adatok = []
with open('autok_listaja.txt', 'r', encoding='utf-8') as fajl:
    for sor in fajl:
        # strip() metódus eltávolítja a sorvégi \n-t
        adatok.append(sor.strip())


'''
A 'autok' nevű lista 'auto' nevű szótár típusokat fog tartalmazni,
egy autó adatait egy szótár tárolja
'''
auto = {}  # egy auto adatai
autok = []  # szótárakat tartalmazó lista
for elem in adatok:
    auto_adatai = elem.split()
    auto['rendszam'] = auto_adatai[0]
    auto['marka'] = auto_adatai[1]
    auto['tipus'] = auto_adatai[2]
    auto['kor'] = int(auto_adatai[3])
    if auto_adatai[4] == '1':
        auto['javitva'] = True
    else:
        auto['javitva'] = False
    auto['koltseg'] = int(auto_adatai[5])

    autok.append(auto)
    auto = {}  # egy új, üres szótár objektum deklarálása ugyanazon a néven

print(autok)
print('\n')

# ------------- 1. feladat -------------
min = int(auto_adatai[3])
max = int(auto_adatai[3])
for auto in autok:
    if int(auto_adatai[3]) < min:
        min = int(auto_adatai[3])
    if int(auto_adatai[3]) > max:
        max = int(auto_adatai[3])

print('A legöregebb autó:', auto_adatai[3-3], auto_adatai[3-2] + ' ' + auto_adatai[3-1], max, 'éves\n')


# ------------- 2. feladat -------------
print('A már megjavított autók rendszáma:')
javitott_autok = []
for  auto in autok:
    if auto['javitva'] == True:
        print(auto['rendszam'])
print('\n')

#------------- 3. feladat -------------
osszeg = 0
for auto in autok:
    osszeg = osszeg + auto['koltseg']
    atlag = osszeg / len(autok)

print(f'Az egy autóra jutó átlagos javítási költség: {atlag:.0f} Ft')
print('\n')

#------------- 4. feladat -------------
szo = input('Adjon meg egy rendszámot')
for auto in autok:
    if szo == auto['rendszam']:
        for i in range(1):
            if auto['javitva'] == False:
                print('A megadott rendszámú autó a műhelyben van.')
            if auto['javitva'] == True:
                print('A megadott rendszámú autó nincs a műhelyben.')

print('\n')
#------------- 5. feladat -------------
halmaz = set()
szo2 = input('Adjon meg egy betűt!')
for auto in autok:
    for betu in auto['marka'] + auto['tipus']:
        if szo2 == betu or betu == szo2.lower() or betu == szo2.upper():
                halmaz.add(auto['marka'] + ' ' + auto['tipus'])

print('\n'.join(halmaz))