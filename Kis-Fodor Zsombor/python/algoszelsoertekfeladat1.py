numbalist = []

lowestnumba = None
highestnumba = None

numba = ''

while numba != 'X' or numba != 'x':
    numba = input("give numba")
    int(numba)
    numbalist.append(numba)

print(numbalist)