while True:
    import random

    szam = random.randint(1, 5)
    szam2 = int(input("Adj meg egy számot!"))
    if szam == szam2:
        print("Helyes!")
        break
    elif szam2 < szam:
        print("Nagyobb")
        continue
    else:
        print("Kisebb")
        continue
    print("A talált szám: ", szam)