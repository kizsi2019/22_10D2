xs = [2,3,5,7,11,13,17,23,29,31,37,43,47,53]
ah = 0
fh = len(xs)
while True:
    if ah == fh:    # Ha a vizsgált terület üres
        print("üres")

# A következő összehasonlítás a ROI közepén kell legyen
kozep_index = (ah + fh) // 2

# Fogjuk középső indexen lévő elemet
kozep_elem = xs[kozep_index]

#print("ROI[{0}:{1}](méret={2}), próba='{3}', érték='{4}'"
        #       .format(ah, fh, fh-ah, kozep_elem, ertek))

# Hasonlítsuk össze az elemet az adott pozícióban lévővel

if kozep_elem == ertek:
    print(kozep_index)      # Megtaláltuk!
if kozep_elem < ertek:
    ah = kozep_index + 1    # Használjuk a felső ROI-t
else:
    fh = kozep_index        # Használjuk az alsó ROI-t