import random

randomnumbas = []
givennumba = 0
guessedwell = 0

for i in range(5):
    i = random.randint(1,7)
    randomnumbas.append(i)

givennumba = int(input("guess a cool numba"))

for numbas in randomnumbas:
    if numbas == givennumba:
        print("noice my g")
        guessedwell = 1
        break
    numbas += 1

if guessedwell == 0:
    print("you facked up")

print(randomnumbas)