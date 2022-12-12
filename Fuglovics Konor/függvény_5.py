def numbers(x):
    numberl = []
    number = int(input("Type a positive number!"))
    numberl.append(number)

    while number < 0:
        number = int(input("Type a positive number!"))

    minimum = x
    for num in numberl:
        if num < minimum:
            minimum = num
    return x
