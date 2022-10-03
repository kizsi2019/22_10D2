print('1. feladat')
fordulok_szama = int(input('Fordulók száma: '))

print('\n2. feladat')
golkulonbsegek = []
for fordulo in range(1, fordulok_szama + 1):
    aktualis_ertek = int(input(f'{fordulo}. fordulóban a gólkülönbség: '))
    golkulonbsegek.append(aktualis_ertek)

print('\n3. feladat')
gyozelmek = 0
veresegek = 0
dontelenek = 0
for golkulonbseg in golkulonbsegek:
    if golkulonbseg > 0:
        gyozelmek = gyozelmek + 1
    elif golkulonbseg < 0:
        veresegek = veresegek + 1
    else:
        dontelenek = dontelenek + 1
print(f'A szezonban a csapatnak {gyozelmek} győzelme, {veresegek} veresége, {dontelenek} döntetlene volt.')
print(f'A csapatnak a szezonban összesen {gyozelmek * 3 + dontelenek} pontja lett.')

if gyozelmek > veresegek + dontelenek:
    print('A csapatnak több győztes mérkőzése volt, mint veresége és döntelene  együttvéve.')

sikerult = 0
for index in range(fordulok_szama - 1):
    if golkulonbsegek[index] > 0 and golkulonbsegek[index] < golkulonbsegek[index+1]:
        sikerult += 1

if sikerult:
    print(f'A kitűzött célt {sikerult} alkalommal sikerült elérnie a csapatnak.')










