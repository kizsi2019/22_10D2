# Készíts egy programot, amely a felhasználó által megadott egész számról eldönti, hogy
# - csak 3-mal osztható,
# - csak 4-gyel osztható,
# - 3-mal és 4-gyel is osztható,
# - sem 3-mal, sem 4-gyel nem osztható!

number = int(input("Give me a number!"))

if number % 3 == 0 and number % 4 == 0:
    print("Dividable by 3 and 4.")
elif number % 3 != 0 and number % 4 != 0:
    print("Not dividable b 3 and 4.")
elif number % 3 == 0:
    print("Dividable by 3.")
elif number % 4 == 0:
    print("Dividable by 4.")