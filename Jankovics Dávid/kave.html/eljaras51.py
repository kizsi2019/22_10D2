def mezot_rajzol(x,y):
    szam1 = int(input('melyik sorba rajzoljam az x_et'))
    szam2 = int(input('melyik sorba oszlopba az x_et'))
	for sor in range(x):
		for oszlop in range(y):
            if sor == 0 and oszlop == 4:
			    print('x ', end='')
            else:
                print('0', end='')
		print()

mezot_rajzol(3,6)
