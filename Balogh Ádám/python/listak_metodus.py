nyelvek = ['Python', 'C', 'C++', 'Java']

nyelvek.reverse()

#print(nyelvek.index('C'))

#print('C++' in nyelvek)

#nyelvek.append('Python')

#nyelvek_masolat = nyelvek.copy()

#nyelvek.insert(1, 'Go')

#nyelvek.pop()
#torolt_nyelv = nyelvek.pop()

#nyelvek.pop(1)

#del nyelvek[1]

#nyelvek.remove('Python')

#print(len(szam))

paletta = ['kék', 'piros', 'fehér', 'fekete', 'zöld', 'sárga', 'barna', 'piros', 'fehér', 'szürke']

szin = input('Adj meg egy színt!\t')
if szin in paletta:
	print('A megadott szín szerepel a listában.')
else:
	print('A megadott szín nem szerepel a listában.')
    paletta.append(szin)
print('A lista színei:')
for szin in paletta:
	print(szin, end=', ')





















