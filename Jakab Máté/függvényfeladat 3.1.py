def hárommal_oszthatók_száma(list, szam = False):
    for number in list:
        if number % 3 == 0:
            szam = True

        return szam

list = []
number_given = 0
while number_given >=0:
        number_given = int(input("add meg a számot"))
        if number_given >0:
            list.append(number_given)

print(hárommal_oszthatók_száma(list))