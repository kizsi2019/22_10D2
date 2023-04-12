letters = 0
words = 0

with open('Párduc.txt', 'r', encoding='utf-8') as Párduc:
    poem = Párduc.read()
    letters += len(poem)

    magi = "aeiouáéíóöőúüű"
    maginumbers = 0
    for letterios in poem:
        if letterios.lower() in magi:
            maginumbers += 1

    words = len(poem.split())


print(words)
print(letters)
print(maginumbers)