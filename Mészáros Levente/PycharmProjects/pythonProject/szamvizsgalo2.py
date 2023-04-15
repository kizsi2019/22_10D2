szam_str = ''
while len(szam_str) < 5:
    szam_str = input('Adj meg egy legalább 5 számjegyből álló számot! ')

print('\n2.feladat')
if int(szam_str) % 5 == 0 and int(szam_str) % 10 == 0:
    print('A szám osztható öttel és tízzel.')
else:
    print('A szám nem osztható öttel és tízzel.')


print('\n3.feladat')
# print('A szám visszafelé olvasva: ', end='')
# for index in range(len(szam_str) - 1, -1, -1):
#     print(szam_str[index], end='')
print(f'A szám visszafelé olvasva: {szam_str[::-1]}')

print('\n4.feladat')
paros_szamjegyek = []
for szamjegy in szam_str:
    if int(szamjegy) % 2 == 0:
        paros_szamjegyek.append(int(szamjegy))
if paros_szamjegyek:
    print(f'A páros számjegyek növekvő sorrendben: {sorted(paros_szamjegyek)}')

print('\n5.feladat')
ismetlodo_szamjegyek = []
for szamjegy in szam_str:
    if szam_str.count(szamjegy) > 1 and szamjegy not in ismetlodo_szamjegyek:
        ismetlodo_szamjegyek.append(szamjegy)

if ismetlodo_szamjegyek:
    print('Az ismétlődő számjegyek: ', ', '.join(ismetlodo_szamjegyek))

print('\n6.feladat')
for index, szamjegy in enumerate(szam_str, start=1):
    print('x', end='')
    if (len(szam_str) - index) % 3 == 0 and len(szam_str) != index:
        print('.', end='')
