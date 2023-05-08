beker = int(input("Hány óra van most? "))

if beker >= 8 and beker < 16:
    print("A bolt nyitva van.")
    print("Ennyi órád van még oda érni.", 16 - beker)
else:
    print("A bolt zárva van.")