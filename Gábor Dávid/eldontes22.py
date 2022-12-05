szo = "alma"
talalat = False
index = 0

bekeres = input("Adj meg egy betűt! ")
while index < len(szo) and not talalat:
    if bekeres == szo[index]:
        talalat = True
    index = index + 1
print("A megadott szó:", szo)

if talalat:
    print("Van találat! ",index)
else:
    print("Nincs találat!")