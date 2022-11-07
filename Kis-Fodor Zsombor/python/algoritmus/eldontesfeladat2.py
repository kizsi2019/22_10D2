word = "amogus"
guessedletter = 'none'
guessedwell = 0
wrongguesses = 0

while guessedwell == 0:
    guessedletter = input("give letter")
    for letter in word:
        if letter == guessedletter:
            print("noice")
            guessedwell = 1
        else:
            if guessedwell == 0:
                wrongguesses += 1

print('you got', wrongguesses, "wrong guesses")
print(word)