betuk = input("Adj meg egy mondatot!")


if betuk[-1] == "?":
    print("Ez egy kérdőmondat!")
elif betuk[-1] == "!":
    print("Ez egy felkiáltó/óható/felszólító mondat")
elif betuk[-1] == ".":
    print("Ez egy kijelentő mondat!")
else:
    print("Nem adtál meg mondatvégi karaktert!")