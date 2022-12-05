wordlist = []

word = 'X'

while word != '':
    word = input("give word")
    if word != '':
        wordlist.append(word)

shortestword = wordlist[0]
longestword = wordlist[0]

for words in wordlist:
    if word < shortestword:
        shortestword = words;
    if word > longestword:
        longestword = words;

print(wordlist)
print(longestword)
print(shortestword)