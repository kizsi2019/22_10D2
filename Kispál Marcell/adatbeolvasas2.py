with open('Rilke_A_parduc.txt', 'r',encoding='UTF=8') as szoveg:
    vers = szoveg.read()
    betuk_szama = len(vers)
print("A szöveg hossza: ", betuk_szama, "betű.")
magánhanzók = "aeiouáéíöőuúüű"
magánhanzók_száma = 0
for karakter in vers:
    if karakter.lower() in magánhanzók:
        magánhanzók_száma += 1
print("A szöveg magánhanzóinak száma: ", magánhanzók_száma)

szavak_száma = len(vers.split())
print("A vers szavainak száma: ", szavak_száma, ".")