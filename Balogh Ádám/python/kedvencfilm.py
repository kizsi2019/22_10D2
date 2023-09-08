def óraperc(percek):
    óra = percek // 60
    perc = percek % 60
    return str(óra) + ' óra ' + str(perc) + ' perc'

print('Add meg három film címét és hosszát percben!')

for i in range(3):
    cím = input('Add meg a(z) {}. film címét! '.format(i+1))
    hossz = int(input('Hány perces a film? '))
    időtartam = óraperc(hossz)
    print('A(z) {} című film {} hosszú.'.format(cím, időtartam))
