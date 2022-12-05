def legkisebb():
    list = []
    number_given = 0
    while number_given >= 0:
        number_given = int(input('ass'))
        if number_given > 0:
            list.append(number_given)

    min = list[0]
    max = list[0]

    for numbers in list:
        if numbers < min:
            min = numbers
        if numbers > max:
            max = numbers
    return min


print(legkisebb())