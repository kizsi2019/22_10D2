
def legkisebb(szamok):
    min = szamok[0]
    for szam in szamok:
        if szam < min:
            min = szam
    print("A legkisebb szám ez volt: ", min)