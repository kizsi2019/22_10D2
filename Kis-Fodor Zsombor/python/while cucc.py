import random

sex = True
wrong = 0

while sex == True:
    numba = random.randint(-5, 5)

    guess = int(input("give numba"))

    if guess == numba:
        print("correct")
        sex = False
    elif guess > numba:
        print("wronge, numba smaller")
        wrong += 1
    else:
        print("wronge, numbar bigger")
        wrong += 1
    print("the numba was", numba)
print("you guessed it in:", wrong)