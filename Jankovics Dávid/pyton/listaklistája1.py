def draw_grid():
    grid = [["O" for i in range(3)] for j in range(3)]
    coordinates = []
    while True:
        x, y = map(int, input("Enter the coordinates (x y): ").split())
        if x not in range(3) or y not in range(3):
            break
        coordinates.append((x, y))
        for i in range(3):
            for j in range(3):
                if (i, j) in coordinates:
                    grid[i][j] = "+"
        for row in grid:
            print(" ".join(row))

draw_grid()

'''A program létrehozza a grid nevű listát, amely 3x3-as méretű és minden eleme "O". Egy coordinates nevű listát is létrehozunk, amely eltárolja a felhasználó által megadott koordinátákat. Az adatbekérés addig folytatódik, amíg a felhasználó intervallumon kívüli értéket nem ad meg. Az adatbekérést követően a coordinates listában tárolt koordináták helyén a grid listában "+" kerül eltárolásra. Végül a grid lista elemeit összekapcsolva (" ".join(row)) egy sort alkotunk, és ezeket kirajzoljuk a képernyőre.'''