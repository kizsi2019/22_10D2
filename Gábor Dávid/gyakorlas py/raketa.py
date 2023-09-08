indul = int(input("Hány órás visszaszámlálást tervezünk? "))
felfüggesztések = 0

for szám in range(indul, 0, -1):
    print("Visszaszámlálás:",szám)
    valasz = input("Fel kell függeszteni a visszaszámlálást (i/n)? ")
    if valasz == 'i':
        felfüggesztések += 1
print("A rakéta a visszaszámlálást követően ennyi órával indult:",indul + felfüggesztések)