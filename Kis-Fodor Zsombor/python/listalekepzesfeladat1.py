words = ['among', 'us', 'impostor', 'sus']

WORDS = []
for word in words:
    if len(word) >= 3:
        WORDS.append(word.upper())

print(WORDS)

coolerwords = []
x = "trans"

for word in words:
    coolerwords.append(word.capitalize())

print(coolerwords)
print(words)