while True:
    import random

    number = random.randint(1, 5)
    number2 = int(input("Give me a number!"))
    if number == number2:
        print("Correct!")
        break
    elif number2 < number:
        print("Bigger")
        continue
    else:
        print("Smaller")
        continue
    print("The guessed number was: ", number)