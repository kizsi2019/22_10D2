felfuggesztesek = 0
indul = int(input("Hány orás visszaszámlálást tervezünk?"))
for szam in range (indul, 0, -1):
    print("Visszaszámlálás: ", szam)
    felfuggeszt = input("Fel kell függeszteni a visszaszámlálást (i/n)?")
    if felfuggeszt == "i":
        felfuggesztesek += 1
print("A rakéta a visszaszámlálást követően ennyi órával indult: ", indul + felfuggesztesek)