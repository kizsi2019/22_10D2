def divisible3(x, *args):
    hit = x
    index = 0
    while index < len(args) and not hit:
        if args[index] % 3 == 0:
            index = index + 1

    if hit:
        print("There's a number divisible by 3")
    else:
        print("There's no number divisible by 3")


print(divisible3(5, 20, 62, 100))