#paros_szamok = [1, 5, 7, 8, 2, 4, 9]
#print(paros_szamok)
#print('páros számok a listában')
#for szam in paros_szamok:
    #if szam % 2 == 0:
        #print(szam)

#paros_szamok = []
#while (szam := int(input('adj meg egy szűmot!'))) >0:
    #paros_szamok.append(szam)
#for szam in paros_szamok:
    #if szam % 2 == 0:
        #print(szam)

#print('\n')
#print(paros_szamok)

#paros_szamok = []
#for i in range(5):
    #if random_szam % 2 == 0:
        #print(szam)
#print(paros_szamok)

import random
def paros_szamok(szamok):
    parosak = []
    for szam in szamok:
        if szam % 2 == 0:
            parosak.append(szam)
    return parosak

