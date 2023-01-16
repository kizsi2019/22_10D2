nyelvek = ['Python', 'C', 'C++', 'Java']

#nyelvek.sort()
#nyelvek.reverse()
#nyelvek.append('Python')
#nyelvek_masolat = nyelvek.copy()

'''nyelvek_honlapkeszites = ['HTML', 'CSS', 'JavaScript']
nyelvek.insert(1, 'Go')
nyelvek.extend(nyelvek_honlapkeszites)'''

#print(nyelvek)
#print(nyelvek.index('C'))
#print(nyelvek.count('Python'))
#print('C++' in nyelvek)
#print('C#' in nyelvek)

paletta = ['kék', 'piros', 'fehér', 'fekete', 'zöld', 'sárga', 'barna', 'piros', 'fehér', 'szürke']

szin = input('Adj meg egy színt!\t')
if szin in paletta:
	print('A megadott szín szerepel a listában.')
else:
	print('A megadott szín nem szerepel a listában.')

print('A lista színei:')
for szin in paletta:
	print(szin, end=', ')