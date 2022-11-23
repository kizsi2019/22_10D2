#for i in range(10):
    #print(i)

#for i in range(5,9):
    #print(i)

#for i in range(2,20,3):
   #print(i)

#honapok = ['január', 'február', 'március', 'április', 'május', 'június', 'július', 'augusztus']

#index = 1
#for honap in honapok:
    #print(index, honap)
    #index = index + 1


#honapok = ['január', 'február', 'március', 'április', 'május', 'június', 'július', 'augusztus']

#for index in range(len(honapok)):
    #print(index, honapok[index])

'''
honapok = ['január', 'február', 'március', 'április', 'május', 'június', 'július', 'augusztus']

for honap in honapok:
    honap = honap.upper()
    print(honap)
print(honapok)
'''

honapok = ['január', 'február', 'március', 'április', 'május', 'június', 'július', 'augusztus']

for index in range(len(honapok)):
    honapok[index] = honapok[index].upper()
print(honapok)