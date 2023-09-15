polc = []

konyv = {
    'szerző':  '',
    'cím': ''
}

konyv2 = {
    'szerző':  '',
    'cím': ''
}

szerzo = None
cim = None
while szerzo != '':
    cim = input('ad meg a könyv címét')
    szerzo = input('add meg a könyv szerzőjét!')
    if szerzo != '':
        konyv['szerző'] = szerzo
        konyv['cím'] = cim
    if szerzo == '':
        break




polc.append(konyv)
polc.append(konyv2)
print(polc)

