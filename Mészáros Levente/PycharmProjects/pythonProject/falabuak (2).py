print('1.feladat')
fordulok_szama = int(input("Forduók száma: "))

print('\n2.feladat')
golkulonbsegek = []
for fordulo in range(1, fordulok_szama + 1):
    aktualis_ertek = int(input(f'{fordulo}.fordulóban a gólkülönbség: '))
    golkulonbsegek.append(aktualis_ertek)
print(golkulonbsegek)
print('\n3.feladat')
gyozelmek = 0
veresegek = 0
dontetlenek = 0
for golkulonbseg in golkulonbsegek:
    if golkulonbseg > 0:
        gyozelmek += 1
    elif golkulonbseg < 0:
        veresegek += 1
    else:
        dontetlenek += 1

print(f'A szezonban a csapatnak {gyozelmek} győzelme, {veresegek} veresége, {dontetlenek} döntetlene volt.')

print('\n4.feladat')
print(f'A csapatnak összesen {gyozelmek * 3 + dontetlenek} pontja lett')

print('\n5.feladat')
if gyozelmek > veresegek + dontetlenek:
    print('A csapatnak több győztes mérkőzése volt, mint veresége és döntetlene együttvéve')
elif gyozelmek > veresegek + dontetlenek:
    print('A csapatnak kevesebb győztes mérkőzése volt, mint veresége és döntetlene együttvéve')

print('\n6.feladat')
sikerult = 0
for index in range(fordulok_szama - 1):
    if 0 < golkulonbsegek[index] < golkulonbsegek[index + 1]:
        sikerult += 1
if sikerult:
    print(f'A kitűzött célt {sikerult} alkalommal sikerült elérnie a csapatnak')