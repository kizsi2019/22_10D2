NYIT = 8   
ZAR = 16   


ora = int(input("Hány óra van most? "))


if ora >= NYIT and ora < ZAR:
    print("A bolt nyitva van.")
    print("Ennyi órád van még odaérni:", ZAR - ora)
else:
    print("A bolt zárva van.")
