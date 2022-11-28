lists = [1, 4, 6, 12, 20, 36, 60, 100]

hit = False
index = 0
while index < len(lists) and not hit:
    if lists[index] % 3 == 0:
        hit = True
    index = index + 1

if hit:
    print("There's a number divisible by 3")
else:
    print("There's no number divisible by 3")