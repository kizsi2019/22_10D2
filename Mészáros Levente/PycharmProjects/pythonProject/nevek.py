nevek = []

db = 0


nev = None
while nev != '' and db <= 3:
    nev = input("Adj meg egy nevet!")
    db += 1
    if nev != '':
        nevek.append(nev)

    if db == 3:
        print("Már nincs lehetőség újabb név megadására")
        break

print(nevek)
print("Progi vége")

