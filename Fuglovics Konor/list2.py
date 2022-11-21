fruits = []
number = 1

fruit = None
while fruit != '' and number <= 3:
    fruit = input('Add a fruit: ')
    if fruit != '':
        fruits.append(fruit)
    number = number + 1

print("Program Ended!")
print(fruits)
