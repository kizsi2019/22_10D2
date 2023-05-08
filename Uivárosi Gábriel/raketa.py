Ora = int(input("Hány óra van a viszaszámlálásig?"))
T = True
felvügesztések = 0
for orraa in range(Ora):
    print("Enyi Óra van a Rakéta kilövéséig:", Ora)
    Kerdes = input("Fel kell függeszteni a visszaszámlálást (i/n)?")
    if Kerdes == "i":
        felvügesztések = felvügesztések + 1
print("A rakéta a visszaszámlálást követően ennyi órával indult:", Ora + felvügesztések)

