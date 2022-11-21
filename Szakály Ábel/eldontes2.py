import random
szo = "alma"
talalat = False
index = 0
betu = input("Adj meg egy betűt")

szo = input('Adj meg szavakat! Ha kilépnél, a szó helyett csak egy ENTER-t üss!')

szo = None
while szo != '':
    szo = input('Adj meg szavakat! Ha kilépnél, a szó helyett csak egy ENTER-t üss!')
while index < len(szo) and not talalat:
    if betu == szo[index]:
        talalat = True
    index = index + 1
print(szo)
if talalat:
    print("Van talalat!")
else:
    print("Nincs talalat!")