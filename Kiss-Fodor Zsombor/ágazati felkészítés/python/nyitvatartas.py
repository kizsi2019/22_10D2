valasz = int(input("Hány óra van?"))

if valasz >= 8 and valasz < 16:
    print("A bolt nyitva van.")
    hatralevoido = 16 - valasz
    print("Még ennyi időd van oda érni:", hatralevoido)
else:
    print("A bolt zárva van.")