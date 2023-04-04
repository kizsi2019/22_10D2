numbalist = []

numba = ''

while numba != 'X':
    numba = input("give numba")
    if numba != 'X':
        numbalist.append(numba)

lowestnumba = numbalist[0]
highestnumba = numbalist[0]

for numbas in numbalist:
    if numbas > highestnumba:
        highestnumba = numbas
    if numbas < lowestnumba:
        lowestnumba = numbas

print(numbalist)
print(highestnumba)
print(lowestnumba)