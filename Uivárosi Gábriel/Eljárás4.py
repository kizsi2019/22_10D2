def sajt():
    LiSZT = []

    for i in range(3):
        szo = input("Agy Egy Szót !!!!!!!")
        LiSZT.append(szo)
    LegR = len(LiSZT[0])
    aszo = LiSZT[0]
    for szak in LiSZT:
      if len(szak) <\
              LegR:
          LegR = len(szak)
          aszo = szak
    print(aszo, LegR)
sajt()

