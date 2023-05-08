def hourmin(minutes):
    hour = minutes // 60
    minute = minutes - hour * 60
    return str(hour) + " óra" + " " + str(minute) + " perc"

for k in range(3):
    name = input("Add meg a film nevét!")
    leng = int(input("Add meg a film hosszát!"))
    print(f"A film {hourmin(leng)} hosszú")