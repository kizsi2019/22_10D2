import random

lists = []
numbers = False
index = 0

for i in range(5):
    number = random.randint(1, 7)
    lists.append(number)

number = int(input("Adj meg egy számot!"))

while index < len(lists) and not numbers:
    if lists[index] == number:
        numbers = True
    index = index + 1

if numbers:
    print(f"Ez a szám benne van a listában, és ez a szám indexe: {index-1}")
    print(lists)
else:
    print("A szám nincs a listában!")