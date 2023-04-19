hanyora = int(input("Hány óra van most?"))
ido = 16
if 8 < hanyora < 16:
    print("A bolt nyitva van.")
    print("Ennyi időd van még odaérni: ", ido - hanyora)
else:
    print("A bolt zárva van.")