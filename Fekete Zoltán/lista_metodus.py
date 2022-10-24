nyelvek = ['Python', 'C', 'C++', 'Java']

'''nyelvek.reverse()
print(nyelvek)
'''

'''nyelvek_honlapkesziteshez = ['HTML', 'CSS', 'JavaScript']
nyelvek.extend(nyelvek_honlapkesziteshez)
print(nyelvek)
'''

'''nyelvek.insert(1, 'Go')
print(nyelvek)
'''

'''nyelvek.pop()
torolt_nyelv = nyelvek.pop()
print(torolt_nyelv)
'''

'''nyelvek.pop(1)
print(nyelvek)
'''

'''del nyelvek[1]
print(nyelvek)
'''

nyelvek.remove('Python')
print(nyelvek)
nyelvek.append('Python')

szamok = [1, 2, 3, 4, 5]
szavak = ['fal', 'szoba', 'kép', 'villáskulcs']

# megadja, hogy hány elemű a lista
print(len(szamok))

# csak számok esetében használható (különben hibát eredményez)
# összegzi a listában előfroduló számokat
print(sum(szamok))

# a legnagyobb elemet (legnagyobb számot, leghosszabb sztringet) adja eredményül
print(max(szavak))

# a legkisebb elemet (legkisebb számot, legrövidebb sztringet) adja eredményül
print(min(szavak))  