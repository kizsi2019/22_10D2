import random

numbers = []

piece = 0
for i in range(5):
    num = random.randint(1, 10)
    numbers.append(num)
for number in numbers:
    if number % 2 == 0:
        piece = piece + 1

print(numbers)
print(f"Amount of numbers divisible by 2: {piece}")
if piece == 5:
    print("WOW")