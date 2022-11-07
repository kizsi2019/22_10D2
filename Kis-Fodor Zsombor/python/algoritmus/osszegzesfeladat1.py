import random

randomnumbas = []

for i in range(5):
    i = random.randint(1,10)
    randomnumbas.append(i)



allofthem = 0
for numbas in randomnumbas:
    if numbas % 2 == 0:
        allofthem = allofthem + numbas

print(allofthem, 'az összeségük')
print('a lista számai', randomnumbas)