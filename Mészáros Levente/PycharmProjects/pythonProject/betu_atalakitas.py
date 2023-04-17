gyumolcsok = ['ALMA', 'KÖRTE', 'EPER', 'BANÁN']

def atvalto(szo):
    return szo.lower()


atalakitott = list(map(atvalto, gyumolcsok))
print(f'{atalakitott = }')