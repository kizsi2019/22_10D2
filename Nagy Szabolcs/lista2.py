keresztnevek = []
lehetőségek= 1


keresztnev = None
while keresztnev != '' and lehetőségek <= 3:
    keresztnev = input('Adj meg egy keresztnevet! ')
    if keresztnev != '':
        keresztnevek.append(keresztnev)
    lehetőségek = lehetőségek + 1
print("Nincs több lehetőség")
print(keresztnevek)