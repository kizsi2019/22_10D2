def vizsga():

    T = True
    while T == True:

        nev = input("Mi a neve?")
        pont = int(input("Elért ponszám?"))
        if nev == "":
            T = False
        
        elif pont >= 48:
            print(nev, "vizsgája sikeres.")
        else:
            print(nev, " vizsgája sikertelen.")
vizsga()
                



