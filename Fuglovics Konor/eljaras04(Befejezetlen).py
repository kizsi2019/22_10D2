def word():
    words = []
    word1 = input("Write a word!")
    words.append(word1)
    if word1 != "":
        word2 = input("Write a word!")
        words.append(word2)
        if word2 != "":
            word3 = input("Write a word!")
            words.append(word3)
    print(words)

    for letter in words:
        lng = []
        leng = len(letter)
        lng.extend([leng])
        print(lng)


word()
