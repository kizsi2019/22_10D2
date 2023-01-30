num = []
n = int(input("Adj meg egy számot!"))

while n > 0:
    print("Próbáld újra!")
    num.append(n)
    n = int(input("Adj meg egy számot!"))


def mini(num):
    minm = num[0]
    for item in num:
        if item < minm:
            minm = item
    return minm


print(min(num))
