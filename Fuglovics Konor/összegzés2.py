import random

answer = 0
rlist = []

for i in range(5):
    random_number = random.randint(1,10)
    if random_number % 2 == 0:
        answer = answer + random_number
    rlist.append(random_number)

print(rlist)
print(f"The list's answer: {answer}")
