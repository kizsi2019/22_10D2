szo = "kutyafule"
talalat = False
index = 0
betu = input("Adj meg egy számot 1 és 7 között!")
while index < len(szo) and not talalat:
    if betu == szo[index]:
        talalat = True
    index = index + 1
print(szo)
if talalat:
    print("Van talalat!")
else:
    print("Nincs talalat!")