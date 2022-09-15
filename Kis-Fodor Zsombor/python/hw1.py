import random

numba = random.randint(-5, 5)

guess = int(input("give numba"))

if guess == numba:
    print("correct")
elif guess > numba:
    print("wronge, numba smaller")
else:
    print("wronge, numbar bigger")
print("the numba was", numba)