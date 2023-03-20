with open('Rilke_A_parduc.txt', 'r', encoding='utf-8') as text:
    poem = text.read()
    letter_num = len(poem)
print(f"Total characters: {letter_num}")
vowels = "aáeéiíoóöőuúüű"
vow_num = 0
for char in poem:
    if char.lower() in vowels:
        vow_num += 1
print(f"Total vowels: {vow_num}")

word_num = len(poem.split())
print(f"Total words: {word_num}")