osszeg = 0
lista = []

szam = int(input('adj meg szamokat -5 és 5 között'))
while szam < 5 and szam > -5:
    osszeg = osszeg + szam
    lista.append(szam)
    szam = int(input('adj meg szamokat -5 és 5 között'))
print('Összeg', osszeg)
print(lista)