def max_search(x, *args):
    max = x
    for number in args:
        if number > max:
            max = number
    return max


print(max_search(1, 43, 20, 15, 32))