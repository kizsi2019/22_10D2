def rajzol(koordinata):
    racs = [['O ' for x in range(3)] for y in range(3)]
    x, y = koordinata
    racs[x][y] = '+ '
    for sor in racs:
        print(''.join(sor))

while True:
    try:
        x, y = map(int, input("Adja meg a koordinátát (pl.: 0 2): ").split())
        if x in [0, 1, 2] and y in [0, 1, 2]:
            break
        else:
            print("A koordinátáknak 0, 1 vagy 2 értékekkel kell rendelkezniük.")
    except:
        print("Érvénytelen bemenet.")

rajzol((x, y))