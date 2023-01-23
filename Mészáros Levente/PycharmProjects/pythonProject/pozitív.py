def szamok():

    szamok = []
    szam = 0
    while szam >= 0:
        szam = int(input("adj meg egy számot"))
        if szam >= 0:
            szamok.append(szam)

    print(szamok)

    min = szamok[0]
    max = szamok[0]

    for szam in szamok:
        if szam < min:
            min = szam
        if szam > max:
            max = szam

    return min




print(szamok())
