'''
import random

összeg = 0
veletlen_szamok = []
for i in range(5):
    veletlen_szam = random.randint(1,10)
    összeg = összeg + veletlen_szam
    veletlen_szamok.append(veletlen_szam)

print(veletlen_szamok)
print('A lista összege', összeg)
'''

'''
import random

összeg = 0
veletlen_szamok = []
for i in range(5):
    veletlen_szam = random.randint(1,10)
    if veletlen_szam % 2 == 0:
        összeg = összeg + veletlen_szam
    veletlen_szamok.append(veletlen_szam)

print(veletlen_szamok)
print('A lista összege', összeg)
'''