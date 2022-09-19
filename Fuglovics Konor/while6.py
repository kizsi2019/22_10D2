import random

number = 1
pcs = 0
while number <= 20:
    random_number = random.randint(1, 12)
    if random_number % 3 == 0:
        print(random_number)
        pcs += 1
    number += 1
print("Done. This is how many dividable numbers I found:", pcs)
