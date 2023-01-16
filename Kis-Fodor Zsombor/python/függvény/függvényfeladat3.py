def harommal_oszthatok(list, sus = False):
    for numbers in list:
        if numbers % 3 == 0:
            sus = True

    return sus

list = []
number_given = 0
while number_given >= 0:
    number_given = int(input('ass'))
    if number_given > 0:
        list.append(number_given)

print(harommal_oszthatok(list))