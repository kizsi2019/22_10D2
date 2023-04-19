indul = input('hány órás visszaszámlálást tervezünk?')
indult = int(indul)
felfüggesztések = 0

for szám in range(indul, 0, -1):
    print('visszaszámlálás:',szám)
    válasz = input('fel kell függeszteni a visszaszmánlálást (i/n)?')
    if válasz == 'i':
        felfüggesztések +=1
print('A rakéta a visszaszámlálást követően ennyi orával idult:', indul + felfüggesztések)