import random

tárocika = []
for i in range(4):
    randomfosok = []
    for j in range(3):
        egyfos = random.randint(0,25)
        randomfosok.append(egyfos)
    tárocika.append(randomfosok)

print(tárocika)