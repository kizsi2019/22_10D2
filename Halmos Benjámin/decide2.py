szo = "faszkereszt"
talalat = False
index = 0

szam = input("Adj meg egy betüt")

while szam != "":
    szam = input("Adj meg egy betüt")
    while index < len(szo) and not talalat:
        if szam == szo[index]:
            talalat = True
        index = index + 1

if talalat:
    print("Van találat!")
else:
    print("Nincs találat")

print(szo)