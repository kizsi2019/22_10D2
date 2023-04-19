szo1 = input("Agy meg egy szót!")
szo2 = input("meg még egyet")

hosz1 = 0
hosz2 = 0
for betu1 in szo1:
    hosz1 = hosz1 + 1
for betu2 in szo2:
    hosz2 = hosz2 + 1
if hosz1 == hosz2:
    print("A két szó egyforma hoszú")
elif hosz1 > hosz2:
    print(szo1, " A Hoszabb szó")
else:
    print(szo2, " A Hoszabb szó")