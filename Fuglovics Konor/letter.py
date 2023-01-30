word = "almafa"
index = 0
letter = False

betu = input("Adj meg egy betűt!")

while index < len(word) and not letter:
    if word[index] == betu:
        letter = True
    index = index + 1

if letter:
    print("The letter you typed is in the word")
else:
    print("The letter is not in the word!")