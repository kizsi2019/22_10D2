honapok = ['január', 'február', 'március', 'április', 'május']
'''
for honap in honapok:
    honap = honap.upper()
    print(honap)
print(honapok)
'''
for index in range(len(honapok)):
    honapok[index] = honapok[index].upper()
print(honapok)