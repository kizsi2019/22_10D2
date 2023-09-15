import random

randomlist = []
for i in range(10):
    szam = random.randint(1, 50)
    if szam % 4 == 0:
        randomlist.append(szam)

print(randomlist)



