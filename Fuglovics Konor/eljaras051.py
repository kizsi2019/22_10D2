def drawing_area(x, y):
    for row in range(x):
        for column in range(y):
            if row == 0 and column == 4:
                print('x ', end='')
            else:
                print('0 ', end='')
        print()


drawing_area(3, 6)
