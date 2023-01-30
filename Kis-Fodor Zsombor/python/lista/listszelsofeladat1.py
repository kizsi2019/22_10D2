numberlist = []
inputnumber = None

while inputnumber != '':
    inputnumber = int(input('give me numbers'))
    if inputnumber != '':
        numberlist.append(inputnumber)

smallest = inputnumber
biggest = inputnumber

for numbers in numberlist:
    if numbers >= biggest:
        biggest = numbers
    if numbers <= smallest:
        smallest = numbers

print(numberlist)
print('the biggest number is', biggest, 'and the smallest is', smallest)