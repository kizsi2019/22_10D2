honapok = ['januar', 'februar', 'marcius', 'aprilis' ]
#print(honapok)
#print (','.join(honapok))
#print(len(honapok))
#rint(honapok[:3])
gyumolcsok = []
gyumolcs = None
while gyumolcs != '':
    gyumolcs = input('Adj meg egy egy gyümölcsöt!')
    if gyumolcs != '':
        gyumolcsok.append(gyumolcs)
print(gyumolcsok)