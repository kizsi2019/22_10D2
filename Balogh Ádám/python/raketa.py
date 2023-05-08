orak = int(input("Hány órás visszaszámlálást tervezünk? "))
visszaszámlálás = orak
felfuggesztett_orak = 0

while visszaszámlálás > 0:
    print("Visszaszámlálás:", visszaszámlálás)
    felfuggeszt = input("Fel kell függeszteni a visszaszámlálást (i/n)? ")
    if felfuggeszt == "i":
        felfuggesztett_orak += 1
    else:
        visszaszámlálás -= 1

osszes_orak = orak + felfuggesztett_orak
print("A rakéta a visszaszámlálást követően ennyi órával indult:", osszes_orak)
