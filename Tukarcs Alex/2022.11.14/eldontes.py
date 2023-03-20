import random

szo = ""
talalat = False
index = 0
0

betu = input("Adj meg egy betűt! Ha kilépnél, a szó helyett csak egy ENTER-t üss")

while betu != '' and not talalat:
    betu = input("Adj meg egy betűt! Ha kilépnél, a szó helyett csak egy ENTER-t üss")
    if betu == szo[index]:
        talalat = True
    index = index + 1
print(szo)


if talalat:
    print("Van találat!")
else:
    print("Nincs találat!")

print("Program vége!")