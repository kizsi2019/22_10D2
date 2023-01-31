összeg = 0
lista = []
szam = int(input('adj meg egy egész számot -5 és 5 között!'))
while -5> szam > 5:
    összeg = összeg + szam
    list.append(szam)
    szam = int(input('adj meg egy egész számot -5 és 5 között!'))
print('összeg: ', összeg)
print(lista)
