szavak = ['alma', 'barack', 'Attila', 'kávé' 'szekrény']

darab = 0
for szo in szavak:
    if szo[0] == "A" or szo[0] == "a":
        darab = darab + 1
    print ("Ennyi 'a vagy 'A' betűvel kezdődő szó van)