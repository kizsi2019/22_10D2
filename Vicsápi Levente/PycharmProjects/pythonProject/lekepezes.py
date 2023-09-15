sebessegek = ['12.3', '31.7', '28.4', '9.0']

# for ciklus
atalakitott = []
for sebesseg in sebessegek:
    tizedes_tort = float(sebesseg)
    atalakitott.append(tizedes_tort)

print(f'{atalakitott = }')

#listaértelmezés
atalakitott = [float(sebesseg) for sebesseg in sebessegek]
print(f'{atalakitott = }')

#map(fgv, tarolo)

atalakitott = list(map(float, sebessegek))
print(atalakitott)