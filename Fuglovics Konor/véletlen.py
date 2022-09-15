while True:

    import random

    number = random.randint(1, 3)
    number2 = int(input("Give me a number!"))

    if number == number2:
        print("Correct!")
        break
    else:
        print("Try again!")
        continue
