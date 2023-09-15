# Készíts egy függvényt, amely egy adott szöveget vár bemenetként, majd visszaadja a szövegben található szavak számát.
# előre megadott szöveg
def szoveg(text):
    szavak = text.split()
    return len(szavak)
print(szoveg('Hello, Levi vagyok'))

#adatbekéréssel
def szoveg(x, *text):
    szo = input('adj meg egy szöveget')
    szavak = szo.split()
    return len(szavak)
print(szoveg(x=''))

