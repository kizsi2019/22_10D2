lists = []
minimum = lists[0]
maximum = lists[0]
num = int(input('Give me a number!'))
while num != '':
    num = int(input('Give me a number!'))
    lists.append(num)

for number in lists:
    if number < minimum:
        minimum = number
    if number > maximum:
        maximum = number
print(lists)
print(f"The highest number is: {maximum}")
print(f"The lowest number is: {minimum}")
