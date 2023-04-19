def oraperc(percek):
    ora = percek // 60
    perc = percek - ora * 60
    return str(ora) + ' óra ' + str(perc) + ' perc'

for i in range(3):
    cim = input("Add meg egy film címét! ")
    hossz = int(input("Hány perces a film? "))
    print('A(z)', cim, 'című film ', oraperc(hossz), "hosszú")