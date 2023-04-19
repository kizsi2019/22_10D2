szo1 = input("Adj meg egy szót!")
szo2 = input("Ajd meg egy másik szót!")

if len(szo1) == len(szo2):
    print("mind a kettő szó ugyan olyan hosszú")
elif len(szo1) > len(szo2):
    print("a hosszabb szó:", szo1)
else:
    print("a hosszabb szó:", szo2)