import random

szam     = 1
pcs = 0
while szam <= 20:
    random_szam = random.randint(1, 12)
    if random_szam % 3 == 0:
        print(random_szam)
        pcs += 1
    szam += 1
print("Kész, ennyi osztható számot találtam:", pcs)
