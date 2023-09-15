import json
with open('diakok.json', encoding='utf-8') as diak_adatok:
    adatok = json.load(diak_adatok)

print(type(adatok))
for diak in adatok['diakok']:
    print(diak)

with open('diakok_2.json', 'w', encoding='utf-8') as diak_adatok_2:
    json.dump(adatok, diak_adatok_2, indent=2)