colors = ['sárga', 'kék']

newcolor = input("give color")

while newcolor != "":
    if newcolor in colors:
        print('this colors is already in the list', colors.count(newcolor), 'times')
        colors.append(newcolor)
    else:
        colors.append(newcolor)
    print(colors)
    newcolor = input("give color")