folytatja = True
while folytatja:
    print('vidd ki a szemetet')
    valasz = input("Mondjam mégegyszer (i/n)?")
    if valasz == 'n':
        folytatja = False
print('>> Program vége! <<')



szam = int(input("Adj meg egy számot 5 és 10 között"))
while not 5 <= szam <= 10:
    szam = int(input("Helytelen érték, próbáld újra"))
print('Rendben')