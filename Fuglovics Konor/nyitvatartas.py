asktime = int(input("Hány óra van?: "))
closingtime = 16
opentime = 8
timeleft = closingtime - asktime

if asktime >= opentime:
    if asktime < closingtime:
        print("A bolt nyitva van!")
        print(f"Ennyi időd van még: {timeleft}")

if asktime >= closingtime:
    print("A bolt zárva van!")
elif asktime < opentime:
    print("A bolt még nem nyílt meg!")


