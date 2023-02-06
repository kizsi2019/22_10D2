import random
storage = []

for i in range(5):
    lists = []
    for i in range(3):
        number = random.randint(-5, 5)
        lists.append(number)
    storage.append(lists)
print(f"Véletlenszámok: {storage}")

storage2 = 

print("Nem negatív számok:", storage2)