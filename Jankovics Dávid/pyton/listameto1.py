paletta = ['kék', 'piros', 'fehér', 'fekete', 'zöld', 'sárga', 'barna', 'piros', 'fehér', 'szürke']

szin = input('Adj meg egy színt!\t')
if szin in paletta:
	print('A megadott szín nem szerepel a listában.')
else:
	print('A megadott szín ennyiszer szerepel a listában.'), print()

print('A lista színei:')
for szin in paletta:
	print(szin, end=', ')