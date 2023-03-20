tarolo = [['O ' for j in range(3)] for i in range(3)]

def print_grid(grid):
    for row in grid:
        print(" ".join(row))

def change_coordinate(grid, x, y):
    grid[x][y] = '+ '

print_grid(tarolo)

x = int(input("Adja meg az X koordinátát (0-2): "))
y = int(input("Adja meg az Y koordinátát (0-2): "))

change_coordinate(tarolo, x, y)

print_grid(tarolo)
