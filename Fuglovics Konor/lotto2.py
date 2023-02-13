import random

lot = []

for i in range(0, 5):
    num = random.randint(0, 10)
    lot.append(num)

user_lot = []

for j in range(0, 5):
    numbers = int(input("Adj meg egy számot!"))
    if numbers != "":
        numbers.append(user_lot)

print(lot)
print(user_lot)