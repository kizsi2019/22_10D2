import json

with open('diakok.json', 'r', encoding='utf-8') as diak_adatok:
    adatok = json.load(diak_adatok)
    for diak in adatok['diakok']:
        diak['osztaly'] = '10.C'
        print(diak)


with open('.diakok_2.json', 'w', encoding='utf-8') as diak_adatok_2:
    json.dump(adatok, diak_adatok_2, indent=2)

with open('.diakok_2.json', 'r', encoding='utf-8') as bemenet:
    adatok2 = json.load(bemenet)
    for i in adatok2['diakok']:
        print(diak)






