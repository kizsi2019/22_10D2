szam = 1
while szam <= 10:
    print(szam)
    szam = szam +1
szamlalo = 1
while szamlalo <= 5:
    print('anyád!')
    szamlalo = szamlalo +1


folytatja = True
while folytatja:
    print('apád!')
    valasz = input('Mondjam még egyszer?(i/n)')
    if valasz == 'n':
        folytatja = False




szam = int(input('Adj meg egy számot 5 és 10 között! '))
 # while szam < 5 or 10 < szam:
while not 5 <= szam <= 10:
    szam = int(input('Helytelen érték! Adj meg egy számot 5 és 10 között! '))
  
print('Rendben!')     
  