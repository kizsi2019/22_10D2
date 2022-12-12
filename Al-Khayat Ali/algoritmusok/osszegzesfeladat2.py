osszeg = 0
lista = []

szam = int(input('adj meg egy egesz szamot -5 es 5 kozott'))
while szam -5 <= szam < 5:
    osszeg = osszeg + szam
    lista.append(szam)
    szam = int(input('adj meg egy egesz szamot -5 es 5 kozott'))
print('osszeg: ', osszeg)
print(lista)