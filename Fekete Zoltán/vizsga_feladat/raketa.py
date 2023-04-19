ora = int(input("Hány órás visszaszámlálást tervezünk?"))
while ora > 0:
    print("Visszaszámlálás: ", ora)
    ora = ora - 1
    felfuggeszt = input("Fel kell függeszteni a visszaszámlálást (i/n)?")


if felfuggeszt == "i":
    ora = ora + 1
    print("Visszaszamlalas: ", ora)



print("A rakéta a visszaszámlálást követően ennyi órával indult: ", ora)