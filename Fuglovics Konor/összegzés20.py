answer = 0
ilist = []

number = int(input("Give me a number between -5 and 5 !"))
while -5 < number < 5:
    answer += number
    ilist.append(number)
    number = int(input("Give me a number between -5 and 5 !"))
print(ilist)
print(f"Total: {answer}")