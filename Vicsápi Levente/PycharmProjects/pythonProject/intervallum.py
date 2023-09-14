import random
szamok = []

index = 0
for i in range(10):
    szam = random.randint(0, 50)
    if szam % 4 == 0:
        szamok.append(szam)
        index = index + 1

print(szamok)
print('Ennyi elemből áll a lista', index)




