def harommal_oszthatok(x, *szamok):
    szamlalo = 1
    talalat = False
    for i in szamok:
        if i % 3 == 0:
            talalat = True
        if i % 2 == 0:
            talalat = False
        if talalat:
            szamlalo += 1
    return szamlalo

print(harommal_oszthatok(1,3,6,4,10))