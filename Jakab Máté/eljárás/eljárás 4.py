def DefenitonofInsanity():
    smallest = numbers[0]
    for numbas in numbers:
        if numbas < smallest:
            smallest = numbas
    print(smallest)

numbers = []

for i in range(3):
    numba = int(input("give number"))
    numbers.append(numba)


DefenitonofInsanity()