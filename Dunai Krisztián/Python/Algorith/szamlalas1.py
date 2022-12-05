import random

randomnumbas = []

for i in range(5):
    i = random.randint(1,10)
    randomnumbas.append(i)

randomnumbaspartner = []
for numbas in randomnumbas:
    if numbas % 2 == 0:
        randomnumbaspartner.append(numbas)

print('a lista számai', randomnumbas)
print('a lista PÁROS számai', randomnumbaspartner)