def fgv_2(x):
    x[0] += 17


szamok = [1, 2, 3, 4]
print(f'Függvényhívás előtt: {szamok=}')
fgv_2(szamok)
print(f'Függvényhívás után: {szamok=}')

