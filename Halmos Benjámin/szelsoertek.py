lista = [12, 5, 4, 8, 9, 11, 10, 12, 6]

    for szam in lista:
        if szam < min:
            min = szam
        if szam > max:
            max = szam

print("legkissebb fasz méret", min, "cm")
print("legnagyobb fasz méret", max, "cm")