asktime = int(input("Hány óra van?: "))
closingtime = 16
opentime = 8
timeleft = closingtime - asktime
if asktime > closingtime:
    print("A bolt zárva van")
elif asktime < closingtime:
    print("A bolt nyitva van!")
    print(f"Ennyi időd van még: {timeleft}")

