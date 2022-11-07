numbalist = []

lowestnumba = None
highestnumba = None

numba = ''

while numba != 'X' or numba != 'x':
    numba = input("give numba")
    if numba != 'X' or numba != 'x':
        int(numba)
        numbalist.append(numba)

print(numbalist)