szavak = ['alma', 'barack', 'Attila', 'kávé', 'szekrény', 'asztal']

AUUUGH = 0
for AAAs in szavak:
    if AAAs[0] == 'a' or AAAs[0] == 'A':
        AUUUGH += 1

szavakE = ['Elemér', 'Emma', 'ajtó', 'róka', 'egér']
ERR = []
for EEEs in szavakE:
    for E in EEEs:
        if E[0] == 'e' or E[0] == 'E':
            ERR.append(EEEs)

print(ERR)
print(AUUUGH)