import random

numbers = []
nonodd = 0

for i in range(5):
    randomnumber = random.randint(1, 10)
    numbers.append(randomnumber)

for number in numbers:
    if number % 2 == 0:
        nonodd += 1

print(nonodd)
print(numbers)