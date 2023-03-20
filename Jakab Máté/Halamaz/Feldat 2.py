import random

generated_numbers = set(random.sample(range(0, 11), 5))
print("A generált számok:", generated_numbers)

guessed_numbers = set()
while len(guessed_numbers) < 5:
    try:
        number = int(input("Adj meg egy számot [0, 10] intervallumból: "))
        if number in range(0, 11):
            guessed_numbers.add(number)
        else:
            print("Csak [0, 10] intervallumból lehet számot megadni.")
    except ValueError:
        print("Nem egész számot adtál meg.")

print("A kitalált számok:", guessed_numbers)

correct_guesses = generated_numbers & guessed_numbers
print("Helyesen kitalált számok:", correct_guesses)

incorrect_guesses = guessed_numbers - generated_numbers
print("Helytelenül kitalált számok:", incorrect_guesses)

only_generated = generated_numbers - guessed_numbers
print("Csak a generált számok között volt:", only_generated)

not_generated_nor_guessed = set(range(0, 11)) - generated_numbers - guessed_numbers
print("Egyik halmazban sem volt:", not_generated_nor_guessed)