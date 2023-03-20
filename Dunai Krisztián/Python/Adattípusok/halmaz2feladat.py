import random

generated_numbers = set()
while len(generated_numbers) < 5:
    generated_numbers.add(random.randint(0, 10))

guessed_numbers = set()
while len(guessed_numbers) < 5:
    guess = int(input("Adj meg egy számot (0-10): "))
    if guess >= 0 and guess <= 10:
        guessed_numbers.add(guess)

correct_guesses = generated_numbers & guessed_numbers
incorrect_guesses = guessed_numbers - generated_numbers
not_guessed = generated_numbers - guessed_numbers

print(f"Helyesen talált számok: {correct_guesses} ({len(correct_guesses)})")
print(f"Helytelenül talált számok: {incorrect_guesses} ({len(incorrect_guesses)})")
print(f"Generált, de nem talált számok: {not_guessed} ({len(not_guessed)})")
print(f"Semmilyen halmazban nem szereplő számok: {guessed_numbers ^ generated_numbers} ({len(guessed_numbers ^ generated_numbers)})")
