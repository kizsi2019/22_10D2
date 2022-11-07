szavak = ['alma', 'barack', 'Attila', 'kávé', 'szekrény', 'asztal']
Astart = 0
Eamount = 0

for words in szavak:
    if words[0] == 'a' or words[0] == 'A':
        Astart += 1
        print(words, 'starts with either A or a')

for words in szavak:
    for letter in words:
        if letter[0] == 'e' or letter[0] == 'E':
            Eamount += 1
            print(words, 'has e or E in it')