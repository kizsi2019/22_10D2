def func_1(x):
    return 2*x + 3

def func_2(x):
    return 3*x + 1

def main():
    set_1 = set()
    set_2 = set()

    for x in range(0, 11):
        set_1.add(func_1(x))
        set_2.add(func_2(x))

    print("Függvény 1 értékkészlete:", set_1)
    print("Függvény 2 értékkészlete:", set_2)
    print("Metszet:", set_1 & set_2)
    print("Unió:", set_1 | set_2)
    print("Különbség (1 - 2):", set_1 - set_2)
    print("Különbség (2 - 1):", set_2 - set_1)

if __name__ == "__main__":
    main()
