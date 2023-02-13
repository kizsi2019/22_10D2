szavak = ['ajtó','tojás','Ottó','Tamás', 'tép','Tesla','alma','python']
szavak_uj = []
for szo in szavak:
    if szo[0] == "t" or szo[0] == "T":
        szavak_uj.append(szo)
print(szavak_uj)