randomnumbas = []
givennumba = 0

while givennumba >= -5 and givennumba <= 5:
    givennumba = int(input("give numba"))
    if givennumba >= -5 and givennumba <= 5:
        randomnumbas.append(givennumba)

allofthem = 0
for numbas in randomnumbas:
    allofthem = allofthem + numbas

print(allofthem, 'az összeségük')
print('a lista számai', randomnumbas)