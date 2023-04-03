'''
3. Készíts egy függvényt, amely egy adott szöveget vár bemenetként
majd visszaadja a szövegben található szavak számát.
'''

szoveg = input('adjon meg egy szöveget')

szavak_szama = 0
for szavak in szoveg:
    if szavak == ' ':
        szavak_szama += 1

szavak_szama += 1
print('az összes szavak száma:',szavak_szama)