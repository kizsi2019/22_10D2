szinek = ['sárga', 'piros', 'piros' '']

db = 0
db2 = 0
db3 = 1

szin = input('Adj meg egy színt!')


szinek.append(szin)

if szin == szinek[0]:
    db += 1
    db2 += 1



if szin == szinek[1]:
    db += 1
    db2 += 1




if szin == szinek[2]:
    db += 1
    db2 += 1


if szin == szinek[3]:
    db += 1





if szin != szinek[0]:
    db += 0




if szin != szinek[1]:
    db += 0




if szin != szinek[2]:
    db += 0

if szinek[0] == szinek[3]:
    del szinek[3]





if db2 == 0:
    print('Ez egy új szín a listában', szin)












print('Ez a szín ennyiszer van a listában', (db-1))

if db2 > 0:
    print('Ez a szín már szerepel a listában!', szin)




print(', '.join(szinek))












