lists = [2, 5, 9, 12, 17, 28, 51, 112]

hit = False
index = 0
while index < len(lists) and not hit:
    if lists[index] % 3 == 0:
        hit = True
    index = index + 1

    print(f"The index of the number divisible by 3 is: {index-1}")
