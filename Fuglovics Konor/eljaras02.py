def compare():
    number = int(input('Type a number!'))
    if number > 0:
        print("The number is positive!")
    elif number == 0:
        print(f"The number is {number}!")
    else:
        print("The number is negative!")
compare()