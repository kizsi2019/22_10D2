
with open('Rilke_A_parduc.txt', 'r', encoding='utf-8') as szoveg:
    vers = szoveg.read()
    betuk_száma = len(vers)
    maganhangzok = 'aeiouéáíioóöőüúuű'
    maganhangzok_szama = 0
    for karakter in vers:
        if karakter.lower() in maganhangzok:
            maganhangzok_szama += 1

szavak_száma = len(vers.split())
print(f'a szöveg hossza {betuk_száma} karakter')
print(f'összesen  {maganhangzok_szama} magánhangzó van')
print(f'a versben {szavak_száma} szó van')