import random

numlist = []
for i in range(0, 10):
    number = random.randint(1, 3)
    numlist.append(number)
print(numlist)

num = int(input('Give me a number!'))
for i in numlist:
    if numlist[i] == num:
        numlist.remove(numlist[i])
print(numlist)
