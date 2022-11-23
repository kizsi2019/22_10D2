words = ['Elemér', 'Emma', 'ajtó', 'róka', 'egér']

word = 0
for letter in words:
    if letter[0] == 'e' or letter[0] == 'E':
        word = word + 1
        print(letter)
print(f"Amount of words starting with 'E' or 'e': {word}")
