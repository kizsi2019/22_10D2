palette = ['kék', 'piros', 'fehér', 'fekete', 'zöld', 'sárga', 'barna', 'piros', 'fehér', 'szürke']


color = input('Adj meg egy színt!\t')
input_word = palette.count(color)
if color in palette:
	print('A megadott szín szerepel a listában.')
	print(f'A(z) {color} szín ennyiszer szerepel: {input_word}')
else:
	palette.append(color)

print('A lista színei:')
for color in palette:
	print(color, end=', ')