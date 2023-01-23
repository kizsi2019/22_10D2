numbers = []

x = int(input("Type a number!"))
y = int(input("Type another number!"))

if x != "":
    numbers.append(x)

if y != "":
    numbers.append(y)

if x < y or x > y:
    print(f"A nagyobb érték: {max(numbers)}")
elif x == y:
    print("Egyenlő")
