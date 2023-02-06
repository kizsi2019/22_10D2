def pozitiv_szam():
    szamok_listaja = []

    szam = 0
    while szam >= 0:
        szam = int(input("Adj meg egy számot"))
        if szam >=0:
            szamok_listaja.append(szam)
            min = szamok_listaja[0]
            max = szamok_listaja[0]
            for szam in szamok_listaja:
                if szam < min:
                    min = szam
                if szam > max:
                    max = szam

    print("A legkissebb szám:",min)


pozitiv_szam()