with open('Rilke_A_parduc.txt', 'r', encoding='utf8') as szoveg:
    vers = szoveg.read()
    betuk_szama = len(vers)
print("A szöveg hossza:", betuk_szama, "betű.")