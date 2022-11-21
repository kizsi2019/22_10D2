words = ['alma', 'barack', 'Attila', 'kávé', 'szekrény', 'asztal']
word = 0

for letter in words:
    if letter[0] == 'a' or letter[0] == 'A':
        word = word + 1
print(words)
print(f"Amount of words starting with 'A' or 'a': {word}")