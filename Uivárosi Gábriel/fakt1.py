'''
fakt = 1
szam = int(input('SZÁMOT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'))

for i in range(szam):
    fakt = fakt*(i+1)
print(fakt)
'''
'''
pista =[2, 5, 4, 8, 9, 11, 10, 11]
T = False
index = 0
while index < len(pista) and not T:
    if pista[index] % 3 == 0:
        T = True
    index = index + 1
if T:
    print("van")
else:
    print("nincs")
    '''
pista = ['kék', 'zöld', 'piros', 'fehér']
T = False
index = 0
while index < len(pista) and not T:
        if pista[index] == 'piros':
            T = True
        index = index + 1
if T:
    print("van", index-1)
else:
    print("KÉK")
