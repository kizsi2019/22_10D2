temperatures = []

friday = [20, 25, 18]
saturday = [17, 21, 8]
sunday = [22, 24, 10]
monday = [21, 25, 17]

temperatures.append(friday)
temperatures.append(saturday)
temperatures.append(sunday)
temperatures.append(monday)

print(temperatures)

print(temperatures[0])

print(temperatures[0][1])

for days in temperatures:
    for measuring in days:
        print(measuring)
