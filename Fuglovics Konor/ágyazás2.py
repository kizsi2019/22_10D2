row = 1
while row <= 5:
    column = 1
    while column <= 5:
        if column == row:
            print('O ', end='')
        elif column + row == 6:
            print('O ', end='')
        else:
            print('. ', end='')
        column = column + 1
    print('')
    row = row + 1