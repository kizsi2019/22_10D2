twords = ['ajtó','tojás','Ottó','Tamás', 'tép','Tesla','alma','python']

actualtwords = []
for words in twords:
    if words[0] == 't' or words[0] == 'T':
        actualtwords.append(words)

print(actualtwords)