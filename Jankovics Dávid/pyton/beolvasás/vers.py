vers = []
with open('Rilke_A_parduc.txt', 'r', encoding='utf-8') as szoveg:
    vers= szöveg.read()
    betuk_szama = len(vers)
print("A szöveg hossza", betuk_szama, "betü")
magánhangzók = 'aeiouáéíöőüűóú'
magánhangzók_száma = 0
for karakter in vers:
    if karakter.lower() in magánhangzók:
        magánhangzók_száma += 1
print('A magánhangzók száma', magánhangzók_száma)
szavak_száma = len(vers.split())
print('A vers szavainak száma', szavak_száma)