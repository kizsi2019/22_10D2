words = ['ajtó', 'tojás', 'Ottó', 'Tamás', 'tép', 'Tesla', 'alma', 'python']

wordlist = []
for word in words:
    if word[0] == "T" or word[0] == "t":
        wordlist.append(word)
print(wordlist)