import random

generated_numbers = set(random.sample(range(0, 11), 5))
print("A generált számok:", generated_numbers)

guessed_numbers = set(map(int, input("Próbáld meg kitalálni a generált számokat (5 szám, szóközökkel elválasztva): ").split()))
print("A felhasználó által beírt számok:", guessed_numbers)

correct_guesses = generated_numbers & guessed_numbers
incorrect_guesses = guessed_numbers - generated_numbers
not_guessed = generated_numbers - guessed_numbers

print("Helyesen kitalált számok:", correct_guesses)
print("Helytelenül kitalált számok:", incorrect_guesses)
print("Nem kitalált számok:", not_guessed)
print("Nem használt számok:", (set(range(0, 11)) - generated_numbers) - guessed_numbers)
