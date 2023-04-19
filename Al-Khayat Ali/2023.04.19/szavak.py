szo1 = input("Adj meg egy szót!")
szo2 = input('Adj meg egy másik szót!')

if len(szo1)> len(szo2):
    print("A hosszabb szó a(z)" ,szo1)
elif len(szo1) == len(szo2):
    print("a két szó egyforma hosszúságú")
else:
    print("a hosszabb szó a(z)", szo2)