import random
storage = []

for i in range(4):
    lists = []
    for i in range(3):
        number = random.randint(0, 25)
        lists.append(number)
    storage.append(lists)

print(storage)