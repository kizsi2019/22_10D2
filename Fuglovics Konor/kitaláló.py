import random

number = random.randint(1, 5)
number2 = int(input("Give me a number!"))
if number == number2:
    print("Correct!")
elif number2 < number:
    print("Bigger")
else:
    print("Smaller")
print("The guessed number was: ", number)