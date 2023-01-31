osszeg = 0
lista = []
szam = int(input('Adj meg egy egész számot -5 és 5 között!'))
while -5 < szam < 5:
    osszeg = osszeg + szam
    lista.append(szam)
    szam = int(input('Adj meg egy egész számot -5 és 5 között!'))
print('Összeg: ', osszeg)
print(lista)