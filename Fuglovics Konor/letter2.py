word = "almafa"
letter = False
index = 0
yes = 0
no = 0

betu = input("Adj meg egy betűt!")
while betu != "":
    while index < len(word) and not letter:
        if word[index] == betu:
            letter = True
        index = index + 1
    print(word)

if letter:
    print("The letter you typed is in the word")
    yes = yes + 1
    letter = False
else:
    print("The letter is not in the word!")
    no = no + 1
betu = input("Adj meg egy betűt!")
print(f"Correct guesses: {yes}")
print(f"Misses : {no}")