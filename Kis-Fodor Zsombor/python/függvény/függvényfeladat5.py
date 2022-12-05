def legkisebb(list, sus = list[0]):
    for numbers in list:
        if numbers < sus:
            list[numbers] = sus

    return sus

list = []
number_given = 0
while number_given >= 0:
    number_given = int(input('ass'))
    if number_given > 0:
        list.append(number_given)

print(legkisebb(list))