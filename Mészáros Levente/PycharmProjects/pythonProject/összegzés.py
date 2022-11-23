import random

veletlen_szamok = []
összeg = 0

for i in range(5):
    szam = random.randint(1, 10)
    veletlen_szamok.append((szam))
    if szam % 2 == 0:
        összeg = összeg + szam

print(veletlen_szamok)
print(összeg)



