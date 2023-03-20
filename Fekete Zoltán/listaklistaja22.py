def display_grid(grid, x, y):
    for i, row in enumerate(grid):
        for j, value in enumerate(row):
            if i == x and j == y:
                print("+", end=" ")
            else:
                print(value, end=" ")
        print()

tarolo = [["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]]
x = int(input("Adj meg egy x koordinátát (0 és 2 között): "))
y = int(input("Adj meg egy y koordinátát (0 és 2 között): "))
display_grid(tarolo, x, y)