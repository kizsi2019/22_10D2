with open('Rilke_A_parduc.txt', 'r', encoding='utf-8') as szoveg:
    magánhangzók = "aeiouáéióőúűö"
    magánhangzók_száma = 0
    
    for karakter in vers:
        if karakter.lower() in magánhangzók:
            magánhangzók_száma +- 1

print("A szöveg magánhangzóinak száma: ", magánhangzók_száma)
vers = szoveg.read()
betuk_szama = len(vers)
print("A szöveg hossza ", betuk_szama, "betű.")