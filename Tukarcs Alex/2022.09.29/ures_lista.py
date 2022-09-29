napok = []
print("Amint kész vagy, nyomj egy ENTER-t")
nap = None
while nap != '':
    nap = input('Adj meg egy napot! ')
    if nap != '':
        napok.append(nap)

print(napok)