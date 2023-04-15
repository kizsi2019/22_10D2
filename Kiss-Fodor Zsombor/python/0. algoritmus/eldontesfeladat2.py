import random

words = ["trams", "amogus", "transformers", "rally", "Firebird"]
word = words[random.randint(0,4)]
if word == "trams":
    print("\u001b[31m funny transport")
elif word == "amogus":
    print("\u001b[32m a meme based off a hit 2018 game")
elif word == "transformers":
    print("\u001b[33m a more than 40 year old franchise based on robot toys")
elif word == "rally":
    print("\u001b[32m a type of a car race, usually happening on dirt")
else:
    print("\u001b[33m a word similar to Phoenix, it was also a name for a muscle car")

print("\u001b[37m ------")
print("guess ONE letter from these words!!")
print("------")

guessedletter = 'none'
guessedwell = 0
wrongguesses = 0

while guessedwell == 0:
    guessedletter = input("give letter")
    for letter in word:
        if letter == guessedletter:
            print("------")
            print("you got it right! the word was:", word, "!")
            guessedwell = 1
    if guessedwell == 0:
        wrongguesses += 1

print('it took you', wrongguesses, "tries to get one letter right")

