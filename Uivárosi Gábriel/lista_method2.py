paletta = ['kék', 'piros', 'fehér', 'fekete', 'zöld', 'sárga', 'barna', 'piros', 'fehér', 'szürke']

szin = input('Adj meg egy színt!\t')
if szin in paletta:
	print('A megadott szín szerepel a listában.')
    D = paletta.count(szin)
    print(D)
else:
    print('A megadott szín nem szerepel a listában.')

print('A lista színei:')
for szin in paletta:
	print(szin, end=', ')