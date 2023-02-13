def function1(x):
    return 2 * x + 3


def function2(x):
    return 3 * x + 1


def main():
    set1 = set()
    set2 = set()
    for x in range(0, 11):
        set1.add(function1(x))
        set2.add(function2(x))

    print("Function 1 values: ", set1)
    print("Function 2 values: ", set2)
    print("Intersection: ", set1.intersection(set2))
    print("Union: ", set1.union(set2))
    print("Difference (function 1 - function 2): ", set1.difference(set2))


if __name__ == "__main__":
    main()