print('1.feladat')
print('győzelem: 1, vereség: 2, döntetlen: x \nA heti fordulók eredményeit egy karaktersorozat formájában adja meg!')
eredmeny = input("Adja meg a kosárlabdacsapat eredményét!")

print('\n2.feladat')
fordulok_szama = 0
veresegek_szama = 0
for betu in eredmeny:
    if betu == '2':
        veresegek_szama += 1
    fordulok_szama += 1

print(f'A fordulók száma: ', end='')
print(fordulok_szama)
print(f'A vereségek száma: ', end='')
print(veresegek_szama)

print('\n3.feladat')
osszpontszam = 0
for betu in eredmeny:
    if betu == '1':
        osszpontszam += 3
    elif betu == 'x':
        osszpontszam += 1
    else:
        osszpontszam += 0

print('A fordulók során szerzett összpontszám: ', end='')
print(osszpontszam)

print('\n4.feladat')
# xxx112x1xx111
# 1111x2x1

gyozelmi_szeria = 0
for index in range(len(eredmeny) - 1):
    if eredmeny[1] == '1' and eredmeny[index + 1] == '1' or eredmeny[index] == '1' and eredmeny[index + 1] == '1':
        gyozelmi_szeria += 1

print(f'A leghosszabb győzelmi széria {gyozelmi_szeria} fordulón át tartott.')

print('\n5.feladat')
sorozat = 0
index = 0
for betu in range(len(eredmeny) - 1):
    if eredmeny[index] == '2' and eredmeny[index + 1] == 'x' and eredmeny[index + 2] == '1':
        print('Volt vereség-döntetlen-győzelem hármas a szezonban.')
        print('Ezután nem volt több mérkőzés.')
        sorozat = True

    index += 1

