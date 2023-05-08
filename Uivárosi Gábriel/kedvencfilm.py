def konverzio(percek):
    óra = percek // 60
    perc = percek - óra * 60
    return  str(óra) +'óra ' + str(perc) + 'perc '
for index in range(3):
    cim = input("Film Címe")
    hosza = int(input("Hány perces?"))
    print('A(z)', cim, "Című film Hosza", konverzio(hosza))