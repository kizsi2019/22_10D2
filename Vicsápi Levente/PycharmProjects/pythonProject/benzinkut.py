benzint_eladva = 0
diesel_eladva = 0
db = 0

while True:
    adat = input("Kérem az eladott üzemanyagot (pl. B20 vagy D43), vagy üssön ENTER-t a kilépéshez: ")
    if not adat:
        break

    mennyiseg = int(adat[1:])
    if adat[0] == 'B':
        benzint_eladva += mennyiseg
    elif adat[0] == 'D':
        diesel_eladva += mennyiseg

    db += 1

print(f"\nÖsszesen {db} tankolás történt a következők szerint:")
print(f"{benzint_eladva} liter benzin került eladásra.")
print(f"{diesel_eladva} liter diesel került eladásra.")
