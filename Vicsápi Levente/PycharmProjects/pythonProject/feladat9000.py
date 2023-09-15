n = 7

for i in range(1,2*n): # 2*7
    for j in range(1,2*n): # 2*7
        if i == j or i+j == 2*n: # i+j=14 2*n=14
            print('*', end='')
        else:
            print(' ', end='')
    print()