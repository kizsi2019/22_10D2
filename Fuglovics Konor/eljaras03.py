def similar():
    num1 = int(input("Type a number!"))
    if num1 != "":
        num2 = int(input("Type a number!"))
    if num1 < num2:
        print("The 2nd number is bigger than the 1st one.")
    elif num1 == num2:
        print("Both of them are equal.")
    else:
        print("The 1st number is bigger than the 2nd number.")
similar()
