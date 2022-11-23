print('Ez a program kiszámolja az átlagodat.')
print('Ha már nem akarsz több jegyet megadni, írj 0-át!')
print('--------------------------------------------')

darab = 0
osszeg = 0

erdemjegy = int(input('Add meg az első érdemjegyet: '))
while erdemjegy != 0:
    darab = darab + 1
    osszeg = osszeg + erdemjegy
    erdemjegy = int(input('Add meg az következő érdemjegyet: '))

if darab != 0:
    print('A jegyeid átlaga: ', osszeg / darab)
else:
    print('Nem adtál meg egy jegyet sem!')