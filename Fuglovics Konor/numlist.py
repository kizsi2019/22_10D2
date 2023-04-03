numbers = []

for i in range(10):
    num = random.randint(1, 100)
    numbers.append(num)

for n in numbers:
    if n % 2 == 0:
        print(n)