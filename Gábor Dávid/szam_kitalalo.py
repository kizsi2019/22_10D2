import random
szam = random.randint(1, 5)
bekeres = int(input("Adj meg egy számot! "))

if szam == bekeres:
    print("Eltaláltad")
elif szam > bekeres:
    print("Kisebb")
else:
    print("Nagyobb")
print("A legenerált szám: ",szam)