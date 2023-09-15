adatok = []
with open('diak_adatok.txt', 'r', encoding='utf-8') as celfajl:
    for sor in celfajl:
        adatok.append(sor.strip())

print(adatok)
diak = {}
diakok = []
for elem in adatok:
    diak_adatok = elem.split()
    diak['vezeteknev'] = diak_adatok[0]
    diak['keresztnev'] = diak_adatok[1]
    diak['eletkor'] = int(diak_adatok[2])
    diak['osztaly'] = diak_adatok[3]
    if diak_adatok[4] == '1':
        diak['kollegista'] = True
    else:
        diak['kollegista'] = False
    diakok.append(diak)
    diak = {}
print(diakok)

print('10.A osztályos tanulók:')
for diak in diakok:
    if diak['osztaly'] == '10.A':
        print(diak['vezeteknev'] + ' ' + diak['keresztnev'])

osztaly_10B = [diak for diak in diakok if diak['osztaly'] == '10.B']
print(osztaly_10B)


osszeg = 0
for diak in diakok:
    osszeg = osszeg + diak['eletkor']
atlag = osszeg / len(diakok)
print(f'A diákok életkorának átlaga {atlag:.2f}')